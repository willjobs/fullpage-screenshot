Python script to take a screenshot of a full webpage (vertically; does not scroll horizontally).

This was adapted from https://stackoverflow.com/a/41745378/6591527. ihightower's implementation did not take into account device scaling. This implementation does; however, it does not include any horizontal scrolling, as it wasn't necessary for my use case and caused problems. A future implementation could re-incorporate that functionality.

Tested in Firefox