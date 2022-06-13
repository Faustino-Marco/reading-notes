# LOCAL STORAGE FOR WEB APPS

## Diving In

- persistent local storage has been an advantage held by native client apps over web apps 
- native apps
  - os typically provides an abstraction layer for storing and retrieving app-specific data (prefs, runtime state).
  - stored in registry, INI files, XML files, or somwhere else
- web apps
  - historically lacked these features
  - cookies downsides
    - included with every HTTP request
      - slowing down app
      - sending data unencrypted over web
    - limited to about 4KB data
      - enough to slow down app, but not useful
- solutions before HTML5
  - explorer first
  - adobe flash 6 (flash cookies)
    - allows brief storage up to 100KB
- local/DOM storage
  - Persistent local storage,
  - no need to send unencrypted over the web
  - implemented natively in browsers, available even when other browser plugins aren't
  - almost all browsers support html5
- check for HTML5 Storage:

```html
function supports_html5_storage() {
  try {
    return 'localStorage' in window && window['localStorage'] !== null;
  } catch (e) {
    return false;
  }
}
Instead of writing this function yourself, you can use Modernizr to detect support for HTML5 Storage.

if (Modernizr.localstorage) {
  // window.localStorage is available!
} else {
  // no native support for HTML5 storage :(
  // maybe try dojox.storage or a third-party solution
}
```

- getItem(), setItem(),
```js
var foo = localStorage.getItem("bar");
//...
localStorage.setItem("bar", foo);
```

explanation continued [here](http://diveinto.html5doctor.com/storage.html).


