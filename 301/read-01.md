# Class 01 Reading: Intro to React & Components

## [Component-Based Architechture](https://www.tutorialspoint.com/software_architecture_design/component_based_architecture.htm)

1. What is a "component?"

  >A component is a modular, portable, replaceable, and reusable set of well-defined functionality that encapsulates its implementation and exports it as a higher-level interface.

  - Object-oriented view
    - component is viewed as a set of one or more cooperating classes
      - domain class (analysis)
      - infrastructure class (design)
      - define interfaces that enable classes to communicate and cooperate
  - Conventional view
    - viewed as a functional element or module of a program
    - integrates processing logic, required data structures, and interface enabling component to be invoked and data to be passed to it
  - Process-related view
    - builds from existing components in a library
    - components selected from the library and used to populate the architechture
  - EG. UI component includes grids, buttons (controls)
  - utility components expose a specific subset of functions used in other components.
  - Other: resource intensive, not frequently accessed
    - must be activated using just-in-time (JIT)

2. What are the characteristics of a component?
  - Reusability
    - different situations/applications
  - Replaceable
    - may be freely substituted with other similar components
  - not context specific
    - different environments/contexts
  - extensible
    - can be extended from existing componenets to provide new behavior
  - encapsulated
    - component depicts the interfaces, which allow caller to use its functionality
    - no exposure of details of the internal process or any internal variables or state
  - independent
    - designed to have minimal dependencies on other components

3. What are the advantages of using component-based architecture?
  - Ease of deployment
    - easier to replace existing versions
    - low impact to system/other comps
  - Reduced Cost
    - third party components allows spread cost of dev/maintenance
  - Ease of development
    - defined functionality allows dev without impact
  - Reusable
    - useable across several applications or systems
  - Modification of technical complexity
    - mods complexity through use of component container and its services
  - Reliability
    - increased via reuse of individual component
  - System maintenance and evolution
    - easy to change/update implementation (low impact)
  - independent
    - & flexible connectivity of comps
    - independent dev

## [What is Props and How to Use it in React](https://itnext.io/what-is-props-and-how-to-use-it-in-react-da307f500da0?gi=cdea8469b572#:~:text=%E2%80%9CProps%E2%80%9D%20is%20a%20special%20keyword,way%20from%20parent%20to%20child)

1. What is "props" short for?
  - Special keyword in React
  - short for properties
2. How are props used in React?
  - used for passing data from one component to another
3. What is the flow of props?
  - data with props are being passed ina uni-directional flow (one way from parent to child)

- Props data is read-only
  - data from parent should not be changed by child components

## Things I want to know more about
  - review arrow function syntax in context of props

## Bookmark and Review
- [React Tutorial through ‘Passing Data Through Props’](https://reactjs.org/tutorial/tutorial.html)
- [React Docs - Hello world](https://reactjs.org/docs/hello-world.html)
- [React Docs - Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)
- [React Docs - Rendering elements](https://reactjs.org/docs/rendering-elements.html)
- [React Docs - Components and props](https://reactjs.org/docs/components-and-props.html)