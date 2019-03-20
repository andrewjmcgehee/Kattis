import argparse
import configparser
from datetime import datetime
import json
import multiprocessing as mp
import os
import re
import sys
import time

# check python version
if sys.version_info[0] < 3:
  print("Python 3 required")
  print("Aborting...")
  sys.exit(0)

# set of dependencies
missing_dependencies = {
  "requests",
  "beautiful soup"
}

# import and catch dependency failures
try:
  import requests
  missing_dependencies.remove("requests")
  from bs4 import BeautifulSoup
  missing_dependencies.remove("beautiful soup")
except:
  for d in missing_dependencies:
    print("package \"%s\" required" % d)
  print("Aborting...")
  sys.exit(0)

# global verbose option
verbose = False

# supported programming languages
_suported_langs = {
  "cpp": ".cpp",
  "c++": ".cpp",
  "java": ".java",
  "python": ".py"
}
# convert an extension to a submission language
_extension_to_lang = {
  ".cpp": "C++",
  ".java": "Java",
  ".py": "Python"
}

# headers for submission
_HEADERS = { "User-Agent": "kattis-cli-submit" }

# URLs
_LOGIN_URL = "https://open.kattis.com/login"
_SUBMIT_URL = "https://open.kattis.com/submit"
_STATUS_URL = "https://open.kattis.com/submissions/"

# maximum number of times to check a submissions status
MAX_SUBMISSION_CHECKS = 60

# default size of submission history
DEFAULT_HIST_SIZE = 100

# user config file
user_conf = None

# user conf modified
modified = False

"""
Gets the a problem's rating and sample inputs from kattis

Params: problem_id
Returns: None
"""
def get(problem_id):
  # get programming language and extension
  while True:
    language = input("Programming Language: ").lower()
    if language in _suported_langs:
      extension = _suported_langs[language]
      break
    print("Language \"%s\" not suported..." % language)

  # make GET call for problem rating
  rating = get_problem_rating(problem_id)

  # make GET call for samples zip file
  if verbose:
    print("Making http request: https://open.kattis.com/problems/" + problem_id + "/file/statement/samples.zip")
  r = requests.get("https://open.kattis.com/problems/" + problem_id + "/file/statement/samples.zip")

  # bad request
  if r.status_code != 200:
    print("URL returned non 200 status")
    print("Aborting...")
    sys.exit(0)

  # download and write zip file
  if verbose:
    print("Sample files found!")
    print("Downloading zip file...")
    print()
  with open("samples.zip", mode="wb") as f:
    f.write(r.content)
    f.close()

  # create the directory, unzip the samples, remove the zip file, create the boilerplate file
  if verbose:
    os.system("mkdir -v %s" % problem_id)
    print()
    os.system("unzip samples.zip -d %s" % problem_id)
    print()
    os.system("rm -iv samples.zip")
    print()
    print("Writing boilerplate file...")
    os.chdir(problem_id)
    write_boilerplate(problem_id, extension, rating)
    os.chdir("..")
  else:
    os.system("mkdir -p %s" % problem_id)
    os.system("unzip -q samples.zip -d %s" % problem_id)
    os.system("rm samples.zip")
    os.chdir(problem_id)
    write_boilerplate(problem_id, extension, rating)
    os.chdir("..")

def get_problem_rating(problem_id):
  r = requests.get("https://open.kattis.com/problems/" + problem_id)
  search = re.findall("Difficulty:[ </>a-z]*[0-9]\.[0-9]", r.text)[0]
  rating = search.split('>')[-1]
  return rating

"""
Opens and writes basic boilerplate to a file based on file type

Params: kattis problem id, file extension, problem rating
Returns: None
"""
def write_boilerplate(problem_id, extension, rating):
  # c++ boilerplate
  if extension == ".cpp":
    content =\
"""\
/*
Rating: ~ %s / 10
Link: https://open.kattis.com/problems/%s
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  return 0;
}
""" % (rating, problem_id)

    with open(problem_id + extension, mode="w") as f:
      f.write(content)
      f.close()

  # java boilerplate
  elif extension == ".java":
    content =\
"""\
/*
Rating: ~ %s / 10
Link: https://open.kattis.com/problems/%s
*/

import java.io.*;
import java.util.*;

public class %s {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) {
  }
}
""" % (rating, problem_id, problem_id)

    with open(problem_id + extension, mode="w") as f:
      f.write(content)
      f.close()

  # python boilerplate
  elif extension == ".py":
    content =\
"""\
# Rating: ~ %s / 10
# Link: https://open.kattis.com/problems/%s

def main():

if __name__ == "__main__":
  main()
""" % (rating, problem_id)

    with open(problem_id + extension, mode="w") as f:
      f.write(content)
      f.close()


"""
Runs all the sample inputs for a given kattis problem and checks them for correctness

Params: None
Returns: None
"""
def run():
  file_name = os.path.basename(os.getcwd())
  # find which language to use
  extension = get_source_extension(file_name)
  samples, answers = get_samples_and_answers()
  executable = run_compiler(file_name, extension)
  if executable:
    if samples and answers:
      run_test_cases(executable, samples, answers)
    else:
      print("No sample inputs and answers found")
      print("Aborting...")
      return


def get_source_extension(problem):
  for f in os.listdir():
    base, extension = os.path.splitext(os.path.basename(f))
    if base == problem and extension in _extension_to_lang:
      return extension
  print("No suitable source files found")
  print("Currently Supported Extensions: \".cpp\", \".java\", \".py\"")
  print("Aborting...")
  sys.exit(0)


def get_samples_and_answers():
  samples = []
  answers = []
  for f in os.listdir():
    base, extension = os.path.splitext(os.path.basename(f))
    if extension == ".in":
      samples.append(f)
    if extension == ".ans":
      answers.append(f)
  return (samples, answers)


"""
Helper function for run() method. Compiles the code for compiled languages and checks
existence of interpreter for interpreted languages

Params: source file
Returns: a list of tokens for a system call to run the source code, or None on failure
"""
def run_compiler(file_name, extension):
  status = 1
  if extension == ".cpp":
    # check presence of g++ compiler
    status = os.system("which -s g++")
    if status != 0:
      print("Unable to locate g++ compiler")
      print("Aborting...")
      return None
    # compile the code
    if verbose:
      print("Compiling %s..." % (file_name + extension))
    os.system("g++ -std=c++11 %s" % file_name + extension)
    return ["./a.out"]
  if extension == ".java":
    # check existence of javac compiler
    status = os.system("which -s javac")
    if status != 0:
      print("Unable to locate javac compiler")
      print("Aborting...")
      return None
    # compile the code
    if verbose:
      print("Compiling %s..." % file_name + extension)
    os.system("javac %s" % file_name + extension)
    return ["java", file_name]
  if extension == ".py":
    if verbose:
      print("Trying to infer Python version...")
    version = determine_python_version(file_name + extension)
    if version == 2:
      status = os.system("which -s python2")
      if status != 0:
        print("Unable to locate Python 2 interpreter")
        print("NOTE: Katti only uses the aliases \"python2\" and \"python3\" for python interpreters")
        print("Please make sure the appropriate aliases are in your PATH environment variable")
        print("Aborting...")
        return None
      return ["python2", file_name + extension]
    else:
      status = os.system("which -s python3")
      if status != 0:
        print("Unable to locate Python 3 interpreter")
        print("NOTE: Katti only uses the aliases \"python2\" and \"python3\" for python interpreters")
        print("Please make sure the appropriate aliases are in your PATH environment variable")
        print("Aborting...")
        return None
      return ["python3", file_name + extension]


"""
Runs a given kattis problem through the provided sample inputs - assumes
code is already compiled

Params: list of sample input files, list of expected output files
Returns: None
"""
def run_test_cases(executable, sample_files, expected):
  print("Running test cases...")
  for i, sample in enumerate(sample_files):
    fail = False
    base = '.'.join(sample.split('.')[:-1])
    executable.extend(["<", sample, ">", "test.out"])
    os.system(' '.join(executable))
    status = os.system("cmp test.out %s.ans" % base)
    if status != 0:
      if verbose:
        print("FAIL on sample input %s" % sample)
        print("<<< Expected Output >>>")
        with open(base + ".ans", mode="r") as f:
          print(f.read())
          f.close()
        print("<<< Actual Output >>>")
        with open("test.out", mode="r") as f:
          print(f.read())
          f.close()
      else:
        print("-", end="")
    else:
      if verbose:
        print("PASS on sample input: %s" % sample)
      else:
        print("+", end="")
  os.system("rm *.out 2>/dev/null")
  os.system("rm *.class 2>/dev/null")
  print()


"""
Scans a python file for tokens exclusive to python 2 to infer the python version

Params: a file name to scan
Returns: an integer version of python
"""
def determine_python_version(file_name):
  with open(file_name, mode="r") as f:
    for line in f:
      if "xrange" in line:
        if verbose:
          print("Found occurence of \"xrange\"")
          print("Python 2 inferred\n")
        return 2
      if "raw_input" in line:
        if verbose:
          print("Found occurence of \"raw_input\"")
          print("Python 2 inferred\n")
        return 2
    f.close()
    if verbose:
      print("No tokens exclusive to Python 2 found")
      print("Python 3 inferred\n")
    return 3


"""
Submits a problem to kattis

Params: None
Returns: None
"""
def post():
  config = get_config()
  problem = os.path.basename(os.getcwd())
  extension = get_source_extension(problem)
  lang = _extension_to_lang.get(extension)
  mainclass = problem if extension == ".java" else None

  if lang == "Python":
    version = determine_python_version(problem + extension)
    lang = "Python " + str(version)

  submission_files = [problem + extension]
  try:
    login_response = login(config)
  except requests.exceptions.RequestException as e:
    print("Login Connection Failed:", e)
    sys.exit(0)
  report_login_status(login_response)
  confirm_submission(problem, lang, submission_files, mainclass)

  try:
    submit_response = submit(
      login_response.cookies,
      problem,
      lang,
      submission_files,
      mainclass
    )
  except requests.exceptions.RequestException as e:
    print("Submit Connection Failed:", e)
    sys.exit(0)
  report_submission_status(submit_response)

  plain_text_response = submit_response.content.decode("utf-8").replace("<br />", "\n")
  print(plain_text_response)

  submission_id = plain_text_response.split()[-1].rstrip(".")
  check_submission_status(problem + extension, submission_id)


def check_submission_status(submission_file, submission_id):
  global modified
  print("Awaiting result...\n")
  config = get_config()
  try:
    login_response = login(config)
  except requests.exceptions.RequestException as e:
    print("Login Connection Failed:", e)
    sys.exit(0)
  i = 0
  while i < MAX_SUBMISSION_CHECKS:
    response = requests.get(
      _STATUS_URL + submission_id,
      cookies=login_response.cookies,
      headers=_HEADERS
    )
    soup = BeautifulSoup(response.content, "html.parser")
    status = soup.find("td", class_=re.compile("status"))
    if status:
      status = set(status["class"])
      runtime = soup.find("td", class_=re.compile("runtime"))
      if "accepted" in status:
        accepted = soup.find_all("span", class_=re.compile("accepted"))
        if len(accepted) > 47:
          print("Test Cases: "
                + ("+" * 47)
                + " plus "
                + str(len(accepted) - 47)
                + " more"
          )
        else:
          print("Test Cases: " + ("+" * len(accepted)))
        print("PASSED")
        print("Runtime: %s" % runtime.text)
        user_conf["solved"][submission_file] = True
        modified = True
        break
      elif "rejected" in status:
        accepted = soup.find_all("span", class_=re.compile("accepted"))
        reason = soup.find("span", class_="rejected")
        cases = soup.find_all("span", title=re.compile("Test case"))
        num_cases = cases[0]["title"]
        num_cases = re.findall("[0-9]+/[0-9]+", num_cases)
        num_cases = num_cases[0].split("/")[-1]
        if len(accepted) > 46:
          print("Test Cases: "
                + ("+" * 44)
                + "..."
          )
        else:
          print("Test Cases: " + ("+" * len(accepted)) + "-")
        print("FAILED")
        print("Reason:", reason.text)
        print("Failed Test Case: %i/%s" % (len(accepted)+1, num_cases))
        print("Runtime: %s" % runtime.text)
        break
      else:
        accepted = soup.find_all("span", class_=re.compile("accepted"))
        if len(accepted) > 47:
          print("Test Cases: "
                + ("+" * 47)
                + " plus "
                + str(len(accepted) - 47)
                + " more", end='\r'
          )
        else:
          print("Test Cases: " + ("+" * len(accepted)), end='\r')
        time.sleep(0.5)
        i += 1
    dt = str(datetime.now()).split(".")[0]
    user_conf["history"].insert(0, dt + "\t" + submission_file)
    while len(user_conf["history"]) > user_conf["history_size"]:
      user_conf["history"].pop()
    modified = True


def submit(cookies, problem, lang, files, mainclass=""):
  data = {
    "submit": "true",
    "submit_ctr": 2,
    "language": lang,
    "mainclass": mainclass,
    "problem": problem,
    "tag": "",
    "script": "true"
  }
  submission_files = []
  for i in files:
    with open(i) as f:
      submission_files.append(
        (
          "sub_file[]",
          (
            os.path.basename(i),
            f.read(),
            "application/octet-stream"
          )
        )
      )
  return requests.post(_SUBMIT_URL, data=data, files=submission_files, cookies=cookies, headers=_HEADERS)

def confirm_submission(problem, lang, files, mainclass):
  if verbose:
    print("Problem:", problem)
    print("Language:", lang)
    print("Files:", ", ".join(files))
    print("Submit (Y/N): ", end="")
    if input()[0].lower() != "y":
      print("Aborting...")
      sys.exit(0)
    print()


def report_login_status(response):
  status = response.status_code
  if status == 200 and verbose:
    print("Login Status: 200\n")
    return
  elif status != 200:
    print("Login Failed")
    if verbose:
      if status == 403:
        print("Invalid Username/Token (403)")
      elif status == 404:
        print("Invalid Login URL (404)")
      else:
        print("Status Code:", status)
    sys.exit(0)


def report_submission_status(response):
  status = response.status_code
  if status == 200 and verbose:
    print("Submission Status: 200\n")
    return
  elif status != 200:
    print("Submit Failed")
    if verbose:
      if status == 403:
        print("Access Denied (403)")
      elif status == 404:
        print("Invalid Submission URL (404)")
      else:
        print("Status Code:", status)
    sys.exit(0)


def get_config():
  config = configparser.ConfigParser()
  if not config.read([os.path.join(os.getenv("HOME"), ".kattisrc")]):
    print("Unable to locate .kattisrc file")
    print("Please navigate to https://open.kattis.com/help/submit to download a new one")
    print("Aborting...")
    sys.exit(0)
  return config


def login(config):
  username, token = parse_config(config)
  login_creds = {
    "user": username,
    "token": token,
    "script": "true"
  }
  return requests.post(_LOGIN_URL, data=login_creds, headers=_HEADERS)


"""
Helper function for login. Parses a config file for username and submit token. On failure to parse config file, exits control flow

Params: a config parser object
Returns: a tuple of username and token
"""
def parse_config(config):
  username = config.get("user", "username")
  token = None
  try:
    token = config.get("user", "token")
  except configparser.NoOptionError:
    pass
  if token is None:
    print("Corrupted .katisrc file")
    print("Please navigate to https://open.kattis.com/help/submit and download a new .kattisrc")
    print("Aborting...")
    sys.exit(0)
  return (username, token)


def get_stats():
  if len(user_conf["solved"]) == 0:
    print("You haven't solved any problems yet!")
    return
  solved = list(user_conf["solved"].keys())

  problem_ids = []
  for problem in solved:
    problem_id = problem.split(".")[0]
    problem_ids.append(problem_id)

  # can change to what works best for you
  pool = mp.Pool(processes=64)
  ratings = pool.map(get_numeric_rating, problem_ids)
  pr = (None, 0)
  avg = sum(ratings) / len(solved)
  pool.close()
  pool.join()

  cpp_num = 0
  cpp_denom = 0
  cpp_pr = (None, 0)
  cpp_avg = 0
  java_num = 0
  java_denom = 0
  java_pr = (None, 0)
  java_avg = 0
  py_num = 0
  py_denom = 0
  py_pr = (None, 0)
  py_avg = 0
  for i, problem in enumerate(solved):
    extension = problem.split(".")[-1]
    if extension == "cpp":
      cpp_num += ratings[i]
      cpp_denom += 1
      if ratings[i] > cpp_pr[1]:
        cpp_pr = (problem_ids[i], ratings[i])
      if ratings[i] > pr[1]:
        pr = (problem_ids[i], ratings[i])
    elif extension == "java":
      java_num += ratings[i]
      java_denom += 1
      if ratings[i] > java_pr[1]:
        java_pr = (problem_ids[i], ratings[i])
      if ratings[i] > pr[1]:
        pr = (problem_ids[i], ratings[i])
    elif extension == "py":
      py_num += ratings[i]
      py_denom += 1
      if ratings[i] > py_pr[1]:
        py_pr = (problem_ids[i], ratings[i])
      if ratings[i] > pr[1]:
        pr = (problem_ids[i], ratings[i])
  if cpp_denom != 0:
    cpp_avg = cpp_num / cpp_denom
  if java_denom != 0:
    java_avg = java_num / java_denom
  if py_denom != 0:
    py_avg = py_num / py_denom

  print()
  print("|  LANGUAGE  |   SOLVED   | AVG RATING |               PR               |")
  print("-------------------------------------------------------------------------")
  print("| C++        | %10i | %10.2f | %-26s %3.1f |" % (cpp_denom, cpp_avg, cpp_pr[0], cpp_pr[1]))
  print("| Java       | %10i | %10.2f | %-26s %3.1f |" % (java_denom, java_avg, java_pr[0], java_pr[1]))
  print("| Python     | %10i | %10.2f | %-26s %3.1f |" % (py_denom, py_avg, py_pr[0], py_pr[1]))
  print("-------------------------------------------------------------------------")
  print("| TOTAL      | %10i | %10.2f | %-26s %3.1f |" % (len(solved), avg, pr[0], pr[1]))


def get_numeric_rating(problem_id):
  print("Getting rating for", problem_id + "...")
  return float(get_problem_rating(problem_id))


def get_history():
  if len(user_conf["history"]) == 0:
    print("Your submission history is empty")
    return
  for submission in user_conf["history"]:
    print(submission)


def set_history_size(size):
  global modified
  if os.geteuid() != 0:
    print("NOTE: Requires root access to update config file")
    os.execvp("sudo", ["sudo", "python3"] + sys.argv)
    return
  print("NOTE:")
  print("  - setting the history size is destructive")
  print("  - the history will immediately shrink to the given size")
  print("  - setting the history size to 0 effectively clears your history")
  print()
  ans = input("Do you wish to continue? (Y/N): ")
  if ans.lower() not in {"y", "yes"}:
    return
  user_conf["history_size"] = size
  while len(user_conf["history"]) > size:
    user_conf["history"].pop()
  modified = True


def get_history_size():
  if "history_size" in user_conf:
    return user_conf["history_size"]
  print("Tracking submission history requires that the root kattis directory is set with 'katti --set_root'")
  print("Aborting...")


def handle_history_size(size):
  arg_size = None
  try:
    arg_size = int(size)
    if arg_size < -1:
      raise ValueError
  except ValueError:
    print("Size must be a positive integer value or -1")
    print("Aborting...")
    sys.exit(0)
  if arg_size is not None:
    if arg_size == -1:
      get_history_size()
    else:
      set_history_size(arg_size)


def usage_msg():
  return "katti [-g <problem-id>] [-r] [-p] [-h] [-v]"


def main():
  global verbose, user_conf
  # add command line args
  arg_parser = argparse.ArgumentParser(usage=usage_msg())
  arg_parser.add_argument("-g", "--get", metavar="<problem-id>", help="get a kattis problem by its problem id")
  arg_parser.add_argument("-r", "--run", help="run the test cases for a given problem", action="store_true")
  arg_parser.add_argument("-p", "--post", help="submit a kattis problem", action="store_true")
  arg_parser.add_argument("-v", "--verbose", help="receive verbose outputs", action="store_true")
  arg_parser.add_argument("--stats", help="get kattis stats if possible", action="store_true")
  arg_parser.add_argument("--history", help="see your 50 most recent kattis submissions", action="store_true")
  arg_parser.add_argument("--history_size", metavar="<size>", help="set history size with a number and query history size with ?")
  args = arg_parser.parse_args()

  verbose = args.verbose

  if os.path.exists("/etc/katti.json"):
    user_conf = json.load(open("/etc/katti.json", "r"))
  else:
    user_conf = {
      "solved": dict(),
      "history": [],
      "history_size": DEFAULT_HIST_SIZE
    }

  if args.get:
    get(args.get)
  elif args.run:
    run()
  elif args.post:
    post()
  elif args.stats:
    get_stats()
  elif args.history:
    get_history()
  elif args.history_size:
    handle_history_size(args.history_size)
  else:
    print("usage:", usage_msg())

  if modified:
    write_string = "import os\nimport json\nwith open('/etc/katti.json', 'w') as f:\n\tf.write(json.dumps(%s))" % str(user_conf)
    os.execvp("sudo", ["sudo", "python3", "-c", write_string])

if __name__ == "__main__":
  main()
