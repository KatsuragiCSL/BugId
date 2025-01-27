import json, os, re, sys;

import mRegistry;
from mConsole import oConsole;
from mNotProvided import zNotProvided;

from mColorsAndChars import *;
import mJITDebuggerRegistry;

def fxGetCurrentJITDebuggerCommandLine():
  # Returns a string with the current JIT debugger command line
  # or zNotProvided if no JIT debugger is installed.
  # or None if the registry could not be read or the value makes no sense.
  oRegistryHiveKey = mRegistry.cRegistryHiveKey(
    sHiveName = mJITDebuggerRegistry.sComandLineHiveName,
    sKeyPath = mJITDebuggerRegistry.sComandLineKeyPath,
  );
  o0RegistryValue = oRegistryHiveKey.fo0GetValueForName(sValueName = "Debugger");
  if o0RegistryValue is None:
    return zNotProvided;
  if o0RegistryValue.sTypeName != "REG_SZ":
    return None;
  return oRegistryValue.xValue;