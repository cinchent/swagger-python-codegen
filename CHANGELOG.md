## `swagger-python-codegen` Version History

### Version 0.0.1

Initial release to public.

### Version 0.0.2

* Fixes mis-parsing of `--fix` command-line option.

* Adds `--fix` recipe to allow `multiprocessing.ThreadPool` instance in API
  client object of SDK to be modifiable (supports copying of client object),
  and custom renderer for the API client module to effect that patch.
