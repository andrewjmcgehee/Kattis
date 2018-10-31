import argparse
import os
import sys
import re
import configparser

import requests
import requests.exceptions

_DEFAULT_CONFIG = '/etc/kattis/submit/kattisrc'
_LANGUAGE_GUESS = {
  '.cpp': 'C++',
  '.java': 'Java',
  '.py': 'Python',
}
_GUESS_MAINCLASS = {'Java', 'Python'}
_HEADERS = {'User-Agent': 'kattis-cli-submit'}
LOGIN_URL = 'https://open.kattis.com/login'
SUBMIT_URL = 'https://open.kattis.com/submit'

class ConfigError(Exception):
  pass

def get_url(cfg, option, default):
  if cfg.has_option('kattis', option):
    return cfg.get('kattis', option)
  else:
    return 'https://%s/%s' % (cfg.get('kattis', 'hostname'), default)

def get_config():
  cfg = configparser.ConfigParser()
  if os.path.exists(_DEFAULT_CONFIG):
    cfg.read(_DEFAULT_CONFIG)
  if not cfg.read([os.path.join(os.getenv('HOME'), '.kattisrc'),
                   os.path.join(os.path.dirname(sys.argv[0]), '.kattisrc')]):
    raise ConfigError('Failed to locate .kattisrc\nAborting...')
  return cfg

def login(login_url, username, password=None, token=None):
  login_args = {'user': username, 'script': 'true'}
  if password:
    login_args['password'] = password
  if token:
    login_args['token'] = token
  return requests.post(login_url, data=login_args, headers=_HEADERS)

def login_from_config(cfg):
  username = cfg.get('user', 'username')
  password = token = None
  try:
    token = cfg.get('user', 'token')
  except configparser.NoOptionError:
    pass
  if password is None and token is None:
    raise ConfigError('''\
Your .kattisrc file appears corrupted. It must provide a login token.
Please download a new .kattisrc file.''')
  return login(LOGIN_URL, username, password, token)

def submit(submit_url, cookies, problem, language, files, mainclass=''):
  data = {'submit': 'true',
          'submit_ctr': 2,
          'language': language,
          'mainclass': mainclass,
          'problem': problem,
          'tag': '',
          'script': 'true'
  }
  sub_files = []
  for f in files:
    with open(f) as sub_file:
      sub_files.append(('sub_file[]',
                       (os.path.basename(f),
                       sub_file.read(),
                       'application/octet-stream'))
      )
  return requests.post(submit_url, data=data, files=sub_files, cookies=cookies, headers=_HEADERS)

def confirm_or_die(problem, language, files, mainclass):
  print('Problem:', problem)
  print('Language:', language)
  print('Files:', ', '.join(files))
  print('Submit? (Y/N): ', end='')
  if input()[0].upper() != 'Y':
    print('Aborting...')
    sys.exit(1)

def main():
  files = sys.argv[1:]
  try:
    cfg = get_config()
  except:
    sys.exit(1)

  # problem id and other necessary parameters for POST request
  problem, extension = os.path.splitext(os.path.basename(files[0]))
  language = _LANGUAGE_GUESS.get(extension, None)
  mainclass = problem if language in _GUESS_MAINCLASS else None

  # language to submit as
  if language == 'Python':
    python_version = str(sys.version_info[0])
    try:
      python_version = cfg.get('defaults', 'python-version')
    except configparser.Error:
      pass
    language = 'Python ' + python_version
  if language is None:
    print('Language extension %s not supported' % extension)
    print('Aborting...')
    sys.exit(1)

  # files to submit
  files = list(set(sys.argv[1:]))
  try:
    login_reply = login_from_config(cfg)
  except requests.exceptions.RequestException as err:
    print('Login connection failed:', err)
    sys.exit(1)

  if not login_reply.status_code == 200:
    print('Login failed.')
    if login_reply.status_code == 403:
      print('Incorrect username or password/token (403)')
    elif login_reply.status_code == 404:
      print('Incorrect login URL (404)')
    else:
      print('Status code:', login_reply.status_code)
    sys.exit(1)

  confirm_or_die(problem, language, files, mainclass)

  try:
    result = submit(SUBMIT_URL,
                    login_reply.cookies,
                    problem,
                    language,
                    files,
                    mainclass
    )
  except requests.exceptions.RequestException as err:
    print('Submit connection failed:', err)
    sys.exit(1)

  if result.status_code != 200:
    print('Submission failed.')
    if result.status_code == 403:
      print('Access denied (403)')
    elif result.status_code == 404:
      print('Incorrect submit URL (404)')
    else:
      print('Status code:', login_reply.status_code)
    sys.exit(1)

  plain_result = result.content.decode('utf-8').replace('<br />', '\n')
  print(plain_result)


if __name__ == '__main__':
  main()
