# React 3

## Reading
[Next.js](https://nextjs.org/learn/basics/getting-started)
- Create a Next.js App
    - code bundled using a bundler like webpack 
        - transformed using a compiler like Babel
    - need production optimizations like code splitting
    - may want to statically pre-render some pages for performance, SEO
        - may use server-side rendering or client-side rendering
    - might need server-side code to connect react app to your data store
- Next.js is a React framework
- Setup
    - instlal node.js
    - create app
        - `npx create-next-app [name] --use-npm --example "[directory]"`
    - run dev server
        - `cd [name]`
        - `npm run server`
    - access http://localhost:3000

- Navigate between pages
    - create new file
```js
export default function FirstPost() {
  return <h1>First Post</h1>;
}
```


- links
    - imort Link from next/link;
    h1 tag [see here](https://nextjs.org/learn/basics/navigate-between-pages/link-component)


[React Context for Beginners](https://www.freecodecamp.org/news/react-context-for-beginners/)
- What is React Context
    - allows us to pass down and use (consume) data in whatever component we need in our React app without using props
- when to use
    - passing data that can be used in any component in your app
        - theme data (dark/light mode)
        - user data
            - current auth'd user
        - Location-specific data (language/locale)
- solves props drilling
- how to use
    - create using `createContext` method
    - wrap context provider around component tree
    - put any value on context provider using `value` prop
    - read that value within any component by using the context consumer
- useContext hook
    - instead of using render props, can pass entire context object to React.useContext() to consume context at top of component
```js
import React from 'react';

export const UserContext = React.createContext();

export default function App() {
  return (
    <UserContext.Provider value="Reed">
      <User />
    </UserContext.Provider>
  )
}

function User() {
  const value = React.useContext(UserContext);  
    
  return <h1>{value}</h1>;
}
```
- can't update value that gets passed down???


## Videos
[Why I'm using Next.js in 2020](https://www.youtube.com/watch?v=rtgbaKBhdkk)
- intro
    - framework built on top of react
- background
    - helps in front-end
- performance
    - pre-fetching assets
    - code splitting
        - file-system based routing
        - scalable to thousands of pages
    - polyfils?, webtrack?, etc
- dev experience
    - weback
    - react, fast refresh
        - allows preservation
    - debugging is really nice
    - typescript included
    - css support
    - plugins
- deployment
    - while vercel is great for next.js
    - anywhere with a node server
    - export
        - totally static site
    - redirects/rewrites possible
- community
    - used at 5 of fortune 12 companies
    - next.js engineers are confident about the future of the framework
    - merger of front end/server??
- conclusion


[Learn to use Context in 13 Minutes](https://www.youtube.com/watch?v=5LrDIWkK_Bc)
- hooks
- context values in react fn() components
    - context is for passing down props
- use the useContext hook
    - allow files access to those props via hook

## Bookmark & Review
[Next.js Examples](https://github.com/vercel/next.js/tree/canary/examples)


## TIWKMA
- what kind of experience do programmers need to get jobs working on tools like next.js?