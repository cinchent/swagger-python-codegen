## `swagger-python-codegen` Version History

### Version 0.0.1

Initial release to public.

### Version 0.0.2

* Fixes mis-parsing of `--fix` command-line option.

* Adds `--fix` recipe to allow `multiprocessing.ThreadPool` instance in API
  client object of SDK to be modifiable (supports copying of client object),
  and custom renderer for the API client module to effect that patch.

### Version 0.0.3

* Adds `--fix` recipe to correct non-canonical initial Python module comments
  post-text rendering due to misformatted templates inherited from the public
  `swagger-codegen` release.  This option causes well-formed initial comments
  ti be proiduced, which consist of a U**x-compatible shell script shebang line
  followed by a PEP 263-conformant character encoding specification
  (see `partial_header.mustache`).  All content currently generated presumes
  UTF-8 encoding, but alternate encodings may be supported in the future.
