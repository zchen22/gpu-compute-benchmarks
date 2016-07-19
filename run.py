#!/usr/bin/python

import os, sys
import multiprocessing

def build(benchmark):
  os.chdir(os.path.join(os.getcwd(), benchmark))
  os.system('make')

def clean(benchmark):
  os.chdir(os.path.join(os.getcwd(), benchmark))
  os.system('make clean')

def rebuild(benchmark):
  clean(benchmark)
  build(benchmark)

def run1(benchmark):
  os.chdir(os.path.join(os.getcwd(), benchmark))
  os.system('make run1')

def run2(benchmark):
  os.chdir(os.path.join(os.getcwd(), benchmark))
  os.system('make run2')

def save1(benchmark):
  src_file = os.path.join(os.getcwd(), benchmark, 'bin/sim-func.out')
  dst_file = os.path.join(os.getcwd(), '../results/run1', benchmark + '.out')
  os.rename(src_file, dst_file)

def save2(benchmark):
  src_file = os.path.join(os.getcwd(), benchmark, 'bin/sim-base.out')
  dst_file = os.path.join(os.getcwd(), '../results/run2', 
                          benchmark + '-base.out')
  os.rename(src_file, dst_file)
  src_file = os.path.join(os.getcwd(), benchmark, 'bin/sim-sv.out')
  dst_file = os.path.join(os.getcwd(), '../results/run2', benchmark + '-sv.out')
  os.rename(src_file, dst_file)

def check_cmd_args(valid_args):
  if len(sys.argv) <= 1:
    sys.exit('argc should be >= 2')
  if not sys.argv[1] in valid_args:
    sys.exit('argv[1] is not valid')

def get_benchmarks(benchmarks):
  if len(sys.argv) == 2:
    cwd = os.getcwd()
    for f in os.listdir(cwd):
      if os.path.isdir(f):
        benchmarks.append(f)
  elif len(sys.argv) >= 3:
    for b in sys.argv[2:]:
      benchmarks.append(b)
  benchmarks.sort()

def worker(func_dict, benchmark):
  func_dict[sys.argv[1]](benchmark)

def main():
  func_dict = {'build': build, 'clean': clean, 'rebuild': rebuild,
               'run1': run1, 'run2': run2,
               'save1': save1, 'save2': save2}
  check_cmd_args(func_dict.keys())
  benchmarks = []
  get_benchmarks(benchmarks)
  print len(benchmarks), 'benchmarks:', benchmarks
  for b in benchmarks:
    p = multiprocessing.Process(target = worker, args = (func_dict, b))
    p.start()


if __name__ == '__main__':
  main()

