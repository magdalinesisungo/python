Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> code="ABC123"
>>> name="James"
>>> balance=1000
>>> print(ABC123 confirmed:\n Hi James, your balance is 1000 \n Thank you.
	  
SyntaxError: invalid syntax
>>> code="ABC123"
	  
>>> codecode="ABC123"
	  
>>> name
	  
'James'
>>> balance
	  
1000
>>> code
	  
'ABC123'
>>> print("{}confirmed \n Hi [], your balance is {} \n Thank you.".format(code,name,balance))
	  
ABC123confirmed 
 Hi [], your balance is James 
 Thank you.
>>> print("{}confirmed \n Hi {},your balance is {} \n Thank you.".format(code,name,balance))
	  
ABC123confirmed 
 Hi James,your balance is 1000 
 Thank you.
>>> 
	  
>>> s="Akirachix"
	  
>>> s
	  
'Akirachix'
>>> s[o]
	  
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s[o]
NameError: name 'o' is not defined
>>> s[0]
	  
'A'
>>> s[1]
	  
'k'
>>> s[2]
	  
'i'
>>> s[3]
	  
'r'
>>> s[4]
	  
'a'
>>> s[5]
	  
'c'
>>> s[6]
	  
'h'
>>> s[7]
	  
'i'
>>> s[8]
	  
'x'
>>> s[0:2]
	  
'Ak'
>>> s[:3]
	  
'Aki'
>>> s[:6]
	  
'Akirac'
>>> s[-9]
	  
'A'
>>> s[-9]==s[0]
	  
True
>>> s[-8]
	  
'k'
>>> s[-9:-7]
	  
'Ak'
>>> s[-9:-3]
	  
'Akirac'
>>> s[:-3]
	  
'Akirac'
>>> s[-7:-3]
	  
'irac'
>>> s.index("k")
	  
1
>>> s.index("r")
	  
3
>>> s.index("h")
	  
6
>>> sms="ABC123. Confirmed!Hi Magda,your balance is 1000".
	  
SyntaxError: invalid syntax
>>> sms="ABC123. Confirmed!Hi Magda,your balance is 1000."
	  
>>> sms[0:7]
	  
'ABC123.'
>>> sms[:32]
	  
'ABC123. Confirmed!Hi Magda,your '
>>> sms[:-22]
	  
'ABC123. Confirmed!Hi Magda'
>>> sms[-34:-12]
	  
'med!Hi Magda,your bala'
>>> 
	  
>>> sms[0:7]
	  
'ABC123.'
>>> sms[22:27]
	  
'agda,'
>>> sms[21:27]
	  
'Magda,'
>>> sms[38:33]
	  
''
>>> sms[33:38]
	  
'alanc'
>>> sms[32:39]
	  
'balance'
>>> sms[42:46]
	  
' 100'
>>> sms[42:47]
	  
' 1000'
>>> s.index("Magda")
	  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s.index("Magda")
ValueError: substring not found
>>> s.index("g")
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.index("g")
ValueError: substring not found
>>> 
	  
>>> 
	  
>>> 
	  

>>> 
	  

>>> 
	  

>>> 
	  

>>> sms.upper()
	  
'ABC123. CONFIRMED!HI MAGDA,YOUR BALANCE IS 1000.'
>>> sms.lower()
	  
'abc123. confirmed!hi magda,your balance is 1000.'
>>> sms.capitalize()
	  
'Abc123. confirmed!hi magda,your balance is 1000.'
>>> sms.endswith()
	  
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    sms.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> sms.numeric()
	  
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    sms.numeric()
AttributeError: 'str' object has no attribute 'numeric'
>>> sms.index("c")
	  
37
>>> sms.index("r")
	  
13
>>> sms.endswith("r")
	  
False
>>> sms.replace("1000","10000")
	  
'ABC123. Confirmed!Hi Magda,your balance is 10000.'
>>> len(sms)
	  
48
>>> sms.endswith(".")
	  
True
>>> sms.split()
	  
['ABC123.', 'Confirmed!Hi', 'Magda,your', 'balance', 'is', '1000.']
>>> Akirachix.split
	  
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    Akirachix.split
NameError: name 'Akirachix' is not defined
>>> s.split
	  
<built-in method split of str object at 0x01441408>
>>> s.split()
	  
['Akirachix']
>>> help()
	  

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> "help('string')"
	  
"help('string')"
>>> help(string)
	  
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    help(string)
NameError: name 'string' is not defined
>>> help(str)
	  
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> 
	  
>>> help(keywords)
	  
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined
>>> help
	  
Type help() for interactive help, or help(object) for help about object.
>>> help
	  
Type help() for interactive help, or help(object) for help about object.
>>> help()
	  

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> modules

Please wait a moment while I gather a list of all available modules...

PYTHON              asyncore            html                sched
__future__          atexit              http                scrolledlist
__main__            audioop             hyperparser         search
_abc                autocomplete        idle                searchbase
_ast                autocomplete_w      idle_test           searchengine
_asyncio            autoexpand          idlelib             secrets
_bisect             base64              imaplib             select
_blake2             bdb                 imghdr              selectors
_bootlocale         binascii            imp                 setuptools
_bz2                binhex              importlib           shelve
_codecs             bisect              inspect             shlex
_codecs_cn          browser             io                  shutil
_codecs_hk          builtins            iomenu              signal
_codecs_iso2022     bz2                 ipaddress           site
_codecs_jp          cProfile            itertools           smtpd
_codecs_kr          calendar            json                smtplib
_codecs_tw          calltip             keyword             sndhdr
_collections        calltip_w           lib2to3             socket
_collections_abc    cgi                 linecache           socketserver
_compat_pickle      cgitb               locale              sqlite3
_compression        chunk               logging             squeezer
_contextvars        cmath               lzma                sre_compile
_csv                cmd                 macosx              sre_constants
_ctypes             code                macpath             sre_parse
_ctypes_test        codecontext         mailbox             ssl
_datetime           codecs              mailcap             stackviewer
_decimal            codeop              mainmenu            stat
_dummy_thread       collections         marshal             statistics
_elementtree        colorizer           math                statusbar
_functools          colorsys            mimetypes           string
_hashlib            compileall          mmap                stringprep
_heapq              concurrent          modulefinder        struct
_imp                config              msilib              subprocess
_io                 config_key          msvcrt              sunau
_json               configdialog        multicall           symbol
_locale             configparser        multiprocessing     symtable
_lsprof             contextlib          netrc               sys
_lzma               contextvars         nntplib             sysconfig
_markupbase         copy                nt                  tabnanny
_md5                copyreg             ntpath              tarfile
_msi                crypt               nturl2path          telnetlib
_multibytecodec     csv                 numbers             tempfile
_multiprocessing    ctypes              opcode              test
_opcode             curses              operator            textview
_operator           dataclasses         optparse            textwrap
_osx_support        datetime            os                  this
_overlapped         dbm                 outwin              threading
_pickle             debugger            paragraph           time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple formatter           pydoc_data          weakref
_testmultiphase     fractions           pyexpat             webbrowser
_thread             ftplib              pyparse             window
_threading_local    functools           pyshell             winreg
_tkinter            gc                  query               winsound
_tracemalloc        genericpath         queue               wsgiref
_warnings           getopt              quopri              xdrlib
_weakref            getpass             random              xml
_weakrefset         gettext             re                  xmlrpc
_winapi             glob                redirector          xxsubtype
abc                 grep                replace             zipapp
aifc                gzip                reprlib             zipfile
antigravity         hashlib             rlcompleter         zipimport
argparse            heapq               rpc                 zlib
array               help                rstrip              zoomheight
ast                 help_about          run                 zzdummy
asynchat            history             runpy               
asyncio             hmac                runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
