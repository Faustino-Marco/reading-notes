# React 4

## Reading
[Next.js Dynamic Routes](https://nextjs.org/learn/basics/dynamic-routes)
- Dynamic Routes
    - Page path depends on external data
    - can pre-render pages that depend on external data
    - statically generate pages with dynamic routes
- overview of steps
    - page called `[id].js` under `pages/posts`
    - pages that begin with `[` and end with `]` are dynamic routes
    - export function called `getStaticPaths` from this page
        - in this fn() return a list of possible values for `id`
    - see examples [here](https://nextjs.org/learn/basics/dynamic-routes/page-path-external-data)
- Implement get static paths
    - create file called `[id].js` under `pages/posts`
    - remove `first-post.js`
    - fill in `...` later
    - open `pages/posts/[id].js` in editor and paste code
    - import Layout from `../../components/layout`;
    -
    - export default function Post() {
        return <Layout>...</Layout>;
    }
    - open `lib/posts.js`
    - add following
        - `getAllPostIds` fn()
            - returns list of file names (excluding .md) in the `posts` dir
- Implement getStaticProps
    - [here](https://nextjs.org/learn/basics/dynamic-routes/implement-getstaticprops)
- Render Markdown
    - [here](https://nextjs.org/learn/basics/dynamic-routes/render-markdown)
- Polishing the Post Page
    - [here](https://nextjs.org/learn/basics/dynamic-routes/polishing-post-page)
- Polishing the Index Page
    - [here](https://nextjs.org/learn/basics/dynamic-routes/polishing-index-page)
- Dynamic Routes Details
    - [here](https://nextjs.org/learn/basics/dynamic-routes/dynamic-routes-details)



[Next.js - Deployment](https://nextjs.org/learn/basics/deploying-nextjs-app)
- DPS
    - Deploy
        - Vercel 
            - made by creators of Next.js
            - Defaults for Next.js on Vercel
                - pages using static generation & assets (JS, CSS, images, fonts, etc.)
                    - auto-served from Vercel Edge Network
                    - really fast
                - pages using server-side rendering and API routes will automatically become isolated serverless functions
                    - allows page rendering and PI requests to scale infinitely
            - custom domains
            - env variables
            -auto HTTPS
    - Preview
        - can preview deployment for every push to GH
        - can share preview URL with others for feedback
    - Ship 
        - merged request to main to ship to production
    - Other hosting options [here](https://nextjs.org/learn/basics/deploying-nextjs-app/other-hosting-options)


## Videos
[Next.js 10 is here](https://www.youtube.com/watch?v=JWCS5IdECVI)


## Bookmark & Review
[Next.js Static File Serving](https://nextjs.org/docs/basic-features/static-file-serving)


## TIWKMA
- Just looking forward to linking up the front end to the back end!