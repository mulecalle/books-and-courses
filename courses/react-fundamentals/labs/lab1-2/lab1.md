# Lab 1
In this lab we will be building a simple todo list in React.  There is no Redux piece in today's lab.  The lab is partially copy-paste to get the initial setup but also has some challenging exercises for you. The lab is also a great precursor to lab 2, and will give you a good working reference for how to approach the labs 2/3 , which will be more difficult. This lab also works as a good sanity check of your local dev setup.

Here's a mockup of what our final TodoList might look like:

<img width="331" alt="Screen Shot 2022-09-27 at 8 19 02 PM" src="https://user-images.githubusercontent.com/25653204/192659792-4798d279-2554-4c83-9636-f8c5aad94ed1.png">

- **Required concepts before starting**
  - [ES6 Study Guide](https://github.com/varoonsahgal/react-fundamentals/blob/main/es6studyguide.md)
  - [React Study Guide](https://github.com/varoonsahgal/react-fundamentals/blob/main/reactstudyguide.md)
  - [React Documentation](https://reactjs.org/docs/getting-started.html)
- **What you will learn**
  - How to create React components
  - How React components fit together
  - How to pass data betweeen components

- **Required**
  - All the Milestones below are required
- **Bonus**
  - None right now


## Strategy
Note that we will be giving you the boilerplate for all the components in Milestone 2 - so you will NOT have to create any of these components on your own.

Let’s use the TodoList app mockup above to help us decide how to break the app down into separate React components.
- We’ll need a container component that holds everything - including the actual list of todo items.
- We could say that the input field and add button could be a part of an AddTodo component.
- We would also want a component to hold the list of Todos.
- Each todo item in our list could be it’s own component. The above list would act as a parent component for these todos.
<br/>

So, as we described above the 4 components are:  
- The `TodoApp` component, which acts as a container for everything
- The `AddTodo` component, representing the input field and add button
- The `TodoList` component, representing the list of Todo items
- The `Todo` component, representing each Todo entry

Let’s also throw in a very simple `Title` component that will just display a title for our Todo List

That gives us a total of 5 components.  
<br/>

***Functional pieces of our TodoList***  
Functionally, what would we expect from our Todo list?  Here's a list of features:
- `Add` a new todo to our list
- `Remove` a todo from our list
- An `input` field to add new todo’s.
- Have some form of `storage` to save all the todos in our current list (think React state)

<br/>

Before we start creating components, you should make sure you understand the distinction between
[Presentational and Container components](https://github.com/varoonsahgal/react-fundamentals/blob/main/reactstudyguide.md#presentational-and-container-components)


## Milestone 1: Create React App
For this lab we'll be using a tool built by Facebook to quickly bootstrap a React app. This will allow us to focus on just React. In later labs we'll introduce Redux, Redux Toolkit, along with other more advanced topics as well.

Let's go ahead and generate a new React app using the `create-react-app` tool provided by Facebook. To do so, open the terminal and navigate to a directory where you would like to create the new project - you can call it `rrf-lab1`. **Note:** `create-react-app` will generate a new directory for you with the same name as the app. 

We can use npm's bundled `npx` tool to run binaries from your project's `node_modules`, from your local machine (globally installed) or from the npm central repository. We'll use it to pull the `create-react-app` binary from npm, which allows us to skip installing it globally and guarantees that each time you create a new React app you are using the latest version of the tool.


Once in the appropriate parent directory run:

```bash
$ npx create-react-app rrf-todo
```

> If you are getting certificate errors with Yarn, use npm instead with this command: `npx create-react-app rrf-todo --use-npm`


If you are getting this error indicating that you don't have npx installed, that probably means you need to install node.js, which comes bundled with npm and npx:

<img width="877" alt="Screen Shot 2022-09-27 at 8 54 24 PM" src="https://user-images.githubusercontent.com/25653204/192663250-5b04ad73-350e-45ac-a049-5655f543a97c.png">


To install node.js, you can first install nvm per the script [here](https://github.com/nvm-sh/nvm#installing-and-updating).  Once you install nvm then go ahead and run `nvm install 16` to install node version 16.  Once you install node then you should be set with npm and npx as well.  Go ahead and try running `$ npx create-react-app rrf-todo` again.



Once the install of `create-react-app` completes, change into the project directory and run `yarn start`, like so:

```
$ cd rrf-todo
$ npm start
```

 It should automatically open up [localhost:3000](http://localhost:3000) for you, wherein you will see a small Demo component that's included as part of the app generator.  It will look like this:

<img width="668" alt="Screen Shot 2022-09-27 at 8 38 24 PM" src="https://user-images.githubusercontent.com/25653204/192661761-6c762575-f544-47e2-874f-a9073e240aae.png">


## Milestone 1.5: Clean Up Demo Files
Open up the project in your Javascript editor - the code for that demo component is inside `src/App.js`. The entry point for the app is `src/index.js`. Open `index.js` and let’s take a look at the contents.

Inside the index.js code you’ll see the invocation of `render` with the original demo `App`. This is how a React App is bootstrapped. `root.render` will mount the html element produced by `App` on the specified DOM node, the one with id `root`. You can confirm that node exists by opening up `public/index.html`. You’ll notice the only markup in the `<body>` is:

```html
<div id="root"></div>
```
Don’t be surprised that `index.js` is not referenced inside the `public/index.html` file; create-react-app uses Webpack under the hood to bundle all of your app’s javascript together, by starting at `src/index.js` and following all the `import` statements recursively. Then Webpack injects a script tag into `index.html` for each bundle produced. 

Now let’s clean up the demo code before beginning our app. First, stop your server. Then, delete all the files in the `src` directory except for `index.js`. Since this is the entry point for all of our javascript we’ll still need this. However, we’ll need to remove the references to all the files we deleted. 

Inside your `index.js` file, remove the comments and code after line 13 since we won’t be using that, and remove all the `import` statements except `React` and `ReactDOM`.

The last thing we’ll do is modify the `render` method to use a different component which we will create in the next milestone. Replace `<App />` with `<TodoApp />`, then add an import statement at the top of the file:
```jsx
import TodoApp from './todo-app';
```
Now we're ready to build our app.


## Milestone 2: Component Boilerplate
We will now give you some boilerplate (stub code) for our components. We’ll start with our app container component.

Create a file named `todo-app.jsx` under the `src` directory. The approach we will take is top-down – first we will build out our stateful container components and then we will build out our presentational components.


### Create app container component
Inside your `todo-app.jsx` file copy this code:

```jsx
import React, { Component } from "react";
import Title from "./title";
import AddTodo from "./add-todo";
import TodoList from "./todo-list";

class TodoApp extends Component {
  state = {
    todos: [
      { id: 1, text: 'This is a simple todo list app written in React!' },
      { id: 2, text: 'Hover over todos and click on the `XX` to delete them!' },
      { id: 3, text: 'Add new todos if you like!' },
    ],
  }
    
  // Handler to add a todo
  addTodo = (todo) => {
    // your code here
  }

  // Handler to remove a todo
  removeTodo = (id) => {
    // your code here
  }

  render() {
    return (
      <div>
        <Title />
        <AddTodo handleAdd={this.addTodo} />
        <TodoList todos={this.state.todos} handleRemove={this.removeTodo} />
      </div>
    )
  }
}

export default TodoApp;
```
> Notice how we use public instance class syntax for the component class methods ( an arrow function `addTodo = () => {}` instead of `addTodo() {}`). This pattern is necessary because these methods will likely make a reference to the keyword `this`, which we would expect to resolve to the instance of the `TodoApp` component. In JavaScript, class methods are not bound by default, so when we pass a method reference as a prop to children components (eg. handleAdd to AddTodo and handleRemove to TodoList) the method loses its context. Using the public instance class syntax binds the `this` context so the methods behave as you would expect. See [here](https://reactjs.org/docs/handling-events.html) for more details.

`TodoApp` is our top level component. You can see that our `TodoApp` component will maintain the list of todo items, utilizing React component state. Before hooks were introduced (and used in conjunction with function components), class components were the only way to maintain state. Initializing state in a class component can instead be done inside a constructor, but we are using the alternative class component syntax as we already discussed.

Note that initialization of `state` is the only time you should directly assign the state property. During the component’s lifecycle you should always interact with its `setState` method which triggers React’s rerendering machinery, keeping the UI updated. We’ll use the `setState` method later as we start adding and removing todos.


### Create `AddTodo` component
Inside the render method of `TodoApp`, you can see that we use a component called `AddTodo`. Create a file `add-todo.jsx` for the component inside the `src` directory with the same contents as below. This component will contain a `form` element that the user will use to add todos. The typical pattern for implementing form elements in React is called `controlled components`. We’ll explore that in more detail in a subsequent milestone. For now, take note of the component’s state and the input element’s attributes.

```jsx
import React, { Component } from 'react';

class AddTodo extends Component {
  state = {
    todoText: '',
  }

  handleChange = (event) => {
    // your code here
  }

  handleSubmit = () => {
    // your code here
  }

  render() {
    return (
      <div className="row">
        <input
          type="text"
          value={this.state.todoText}
          placeholder="Add todos here..."
          autoComplete="off"
          onChange={this.handleChange}
        />
        <button onClick={this.handleSubmit}> +</button>
      </div>
    )
  }
}

export default AddTodo;
```
> Notice this is also a class component. We’re using a class to manage the state of the input field. The input field is called a "controlled component". See [here](https://reactjs.org/docs/forms.html#controlled-components) for details.

### Create TodoList component
Next, create a file for the `TodoList` component called `todo-list.jsx`. Add this code to your `todo-list.jsx` file:

```jsx
import React from 'react';
import Todo from './todo.jsx';

const TodoList = ({ todos, handleRemove }) => (
  <div>
    <p><b>Your Todos:</b></p>
    {todos.length > 0 ? (
      todos.map(todo => (
        <Todo todo={todo} remove={handleRemove} key={todo.id} />
      ))
    ) : (
      <h3>No Todos remaining!</h3>
    )}
  </div>
)

export default TodoList;
```

> Because `TodoList` will just ***display*** a list of Todos it receives as `props`, it won't need to maintain any state.  Notice the use of a ternary operator (`condition ? whenTrue : whenFalse`), this is a common React pattern for writing an `if/else` statement in JSX. Notice the use of `map`. This is a classic React pattern for rendering a collection. The `key` prop should be provided since React’s diffing algorithm can optimize rerendering with it. You may see tutorials use the array index as the `key`, which may be fast and simple, but can produce subtle bugs if the position of the elements in the array is not stable. Read more in [the docs](https://reactjs.org/docs/lists-and-keys.html#keys).


### Create Todo component
Note that your `TodoList` component code uses a `Todo` component. Let’s add the stub code for that component as well in a file called, you guessed it, `todo.jsx`:

```jsx
import React from 'react';

const Todo = props => (
  <p>
    {props.todo.text}
    <span
      onClick={()=> {
        //add your code here
      }}>
    <b>&nbsp;XX</b>
    </span>
  </p>
);

export default Todo;
```

> `Todo` represents a single todo item.  It's just a simple presentational component that takes in the todo as prop and then renders  the text as part of the markup. Note that the `<span>` with an `onClick` attribute will be how todos are deleted. You’ll write this logic a bit later.


### Create Title component
Finally, let’s add a simple `Title` component - you’ll notice that we used it in the top level app container. This time you get to try it on your own. Create `title.jsx` and write your code there. Your component needs only to produce the name of your app – maybe `Todo, or not Todo` for something silly, although the perfunctory `Todo List` will do just fine – make it your own!


## Milestone 3: Test the App
Now that all the components are created your code should compile. If you aren’t already, run `yarn start` and go to [http://localhost:3000](http://localhost:3000) where you should see the Todo App running. But nothing really works since we haven’t implemented any of the handlers. Now, your job begins.

Let’s get started on the following exercises to produce a Todo application that works as we described above.


## Milestone 4: Implement handleChange
Taking a look at your Todo list application running at [http://localhost:3000](http://localhost:3000) you'll notice that the `input` field currently doesn’t respond to your input!

The reason it doesn’t work as expected is because we left the `handleChange` event handler blank inside the `AddTodo` component. This is the first functionality for you to complete -- your goal for this milestone is simply to get the `input` field to simply accept some input.

This input element is set up as a Controlled Component. You can read up on [Controlled Components](https://facebook.github.io/react/docs/forms.html) and forms in React to complete this exercise. **Hint:** in the provided component code notice the input field's value attribute is set equal to `this.state.todoText`. Also, make sure that you understand [State in React](https://github.com/varoonsahgal/react-fundamentals/blob/main/reactstudyguide.md#react-state).


## Milestone 5: Implement handleSubmit
Once you get the `<input>` field actually accepting inputs, adding todos still doesn’t work. This is because inside the `AddTodo` component, the `<button>` was assigned `handleSubmit` as its `onClick` handler, but the method is an empty stub. This is the next exercise for you to complete. When the add button is clicked, we need to create a new todo and add it to the list. Remember the list of todos is in the parent `TodoApp` component so we'll need to use a callback to pass data back up to the parent `TodoApp` from `AddTodo`.

**Hints** (click the arrow to reveal)
<details markdown="1">
  <summary>We don’t want to create empty todos.</summary>
  Check for text in the `<input>` field. Try using [trim](http://mdn.io/trim).
</details>
<details markdown="1">
  <summary>Use the props the component is receiving</summary>
  You’ll need the `addTodo` function defined in the parent `TodoApp` component - remember this is being passed as a prop named `handleAdd` to the `AddTodo` component.
</details>
<details markdown="1">
  <summary>Generate a unique ID for each todo</summary>
  A quick and dirty way to generate a unique `id` is to use `Date.now()` which will return a Unix Time Stamp. *Note:* this is adequate for our purposes but not a production app. In production you would either use server-generated IDs or a safer UID generation library like [`shortid`](https://www.npmjs.com/package/shortid).
</details>
<details markdown="1">
  <summary>After adding the todo, what should the input look like?</summary>
  Clear out the `<input>` field's value after the user submits the new todo. Remember this is a controlled component. Refer to [React State](https://github.com/varoonsahgal/react-fundamentals/blob/main/reactstudyguide.md#react-state) if you need a quick refresher on how to manage a component’s state.
</details>


## Milestone 6: Implement addTodo
Unfortunately we still can’t add todos because the `addTodo` function in the `TodoApp` component is also just a stub. In `TodoApp` add the appropriate logic to `addTodo` so that the `todo` passed in as an argument is added to the todo list stored in the component’s state. Make sure you try adding todos and confirm they are appended to your list.

**Hints** (click the arrow to reveal)
<details markdown="1">
  <summary>Don't mutate the existing state</summary>
  Try using the ES6 `spread` operator to produce a new list when a todo is added.  You should be able to get the `addTodo` function to do everything in just one line!
</details>
<details markdown="1">
  <summary>Don't lose existing todos!</summary>
  Be sure to use a reference to the current state when creating an updated list that contains the todo which we are adding.
</details>
<details markdown="1">
  <summary>Rerendering should be triggered automatically</summary>
  Use `setState` to update the component state with your new list and trigger rerendering.
</details>

### Improve Accessibility

Notice that they only way to add a todo is to click the + button; you cannot hit "Enter" as you might expect when your focus is on the `input` field.  This is a bit annoying and can also be a severe accessibility problem; sight-impaired people will not know that the + button will submit the form. It's time to improve that behavior.

The `AddTodo` component is essentially a form, trying to submit some information. Fortunately, submitting forms is an extremely common pattern and we can leverage built-in behavior of the HTML spec to accomplish a lot of behavior for free.

First, inside the `AddTodo` component, change the wrapping `div` element to a `form` element. Add an `onSubmit` prop to the `form` element that takes `this.handleSubmit`.

Next, change the `button` behavior by removing the `onClick` prop and adding a `type="submit"` prop. If you're concerned about no longer being able to click the button, fear not! That's the magic of HTML at work; by telling the button that it's a "submit" button, when it is clicked it simply triggers the `onSubmit` behavior of the form element that we just defined.

Now try out the magic. Type in a todo, press enter, and... it reloaded the page, and our new todo disappeared?!

Ah, there's one more thing to fix. Forms by default will reload the page -- this is a remnant of the original style of web sites, where submitting a form always meant rendering some new page from the server. We need to prevent this default behavior.

Change `handleSubmit` to accept a parameter, `event` (or `e` for short, a canonical shorthand). Normally this `event` would be a `HTMLFormElement: submit event` ([docs](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event)). With React, all events are wrapped in a `SyntheticEvent` for performance purposes ([docs](https://reactjs.org/docs/events.html)). Regardless, all you'll need to do is tell the event to stop its default behavior with `event.preventDefault()`.

<details markdown="1">
  <summary>Try writing the code out yourself, or skip to the answer</summary>

```javascript
class AddTodo extends Component {
  state = {
    todoText: '',
  }

  handleChange = (event) => {
    // your code here
  }

  handleSubmit = (e) => {
    e.preventDefault()
    // your code here
  }

  render() {
    return (
      <form className="row" onSubmit={this.handleSubmit}>
        <input
          type="text"
          value={this.state.todoText}
          placeholder="Add todos here..."
          autoComplete="off"
          onChange={this.handleChange}
        />
        <button type="submit"> +</button>
      </div>
    )
  }
}  
```

</details>

## Milestone 7: Implement removeTodo
Now that we have the add functionality working, we need to implement the remove functionality so that a user can easily remove a todo item from the list by clicking on the `XX` next to each todo item.  

In our component hierarchy, `TodoApp` is the parent of `TodoList` and passes it the function called `removeTodo` as a prop with the name `handleRemove`. Then `TodoList` passes `handleRemove` to the `Todo` component as a prop with the name `remove`.  Note that `TodoList` doesn't do anything with the `handleRemove` callback - it's really just an intermediary in the passage of the callback. So, the handler function gets passed from the `TodoApp` grandparent component down to it's grandchild `Todo`.

### Understanding the design

Why was it designed in this way?  Why are we passing the callback through props two components down in the hierarchy?

Well, our `TodoApp` component is our stateful component which maintains the list of todo items utilizing React component state. The list of todos must be kept at the `TodoApp` level becuase both the `AddTodo` and `TodoList` components depend on that data. Since sibling components can't share data we must promote it to a common parent component. Because `TodoApp` contains the data, it is necessary that the handlers for operating on that data--namely adding and deleting todo items--are defined on this component too, where the data they manipulate is in scope.

But, each todo item in our list is represented by the `Todo` component - a presentational component used to simply display the text for a given todo item and also a delete button. Since this component lacks direct access to the list of todos, the delete button’s click handler needs to use a callback function that *can* access the list. The `TodoApp` grandparent component has access to the list, so the appropriate logic is defined there and passed down the component hierarchy as `props` to ultimately be used by `Todo` in its `onClick` handler.


### Challenge details
Now your challenge is to first implement the `removeTodo` function in `TodoApp`. Then implement `Todo`’s `onClick` using the handler it recieves as a prop.

**Hints** (click the arrow to reveal)
<details markdown="1">
  <summary>How do you specify the todo that is being removed?</summary>
  Notice the `removeTodo` function expects to be invoked with the todo’s `id` as an argument.
</details>
<details markdown="1">
  <summary>Don't mutate the existing state or lose existing todos!</summary>
  Be sure to use reference the current state when creating an updated list without the todo we are removing.
  Try using the [filter array method](http://mdn.io/filter) to produce a *new list* that excludes the specified todo.
</details>
<details markdown="1">
  <summary>Rerendering should be triggered automatically</summary>
  Use `setState` to update the component state with your new list and trigger rerendering.
</details>


## Milestone 8: Destructuring our props
If you take a look at your `Todo` component you'll notice we just have a simple functional component that takes in some `props` and then returns some markup using the `props` data:

```jsx
// our abbreviated Todo component:
const Todo = props => {
  return (
  // use props here to return some JSX...
  // ...
  );
};
```

We could also use ES6 destructuring with our props.  Here's an example of what that would look like:

```jsx
//curly braces for destructuring
const DestructuredComponent = ({prop1, prop2}) => {
  return <h1>Hello, {prop1} {prop2}</h1>;
};
```
Now, your challenge is to implement [ES6 destructuring](https://github.com/varoonsahgal/react-fundamentals/blob/main/es6studyguide.md#es6---destructuring) in the `Todo` component to destructure the props passed in.  That way, your code will be cleaner, and you won't have to access the properties from the `props` object (ie. `props.remove` or `props.todo`). Instead, you can directly reference `remove` and `todo`.


## Milestone 9: Refactoring to use hooks
Hooks are a new addition in React as of version 16.8.  With hooks, we can now use state and other React features without writing a class-based component. Instead we use functional components with hooks to manage state.

Now, your challenge is to modify your `TodoApp` and `AddTodo` component to utilize the `useState` hook to manage your todo array instead of using `setState`.

You can read our [guide on React hooks](https://github.com/varoonsahgal/react-fundamentals/blob/main/reactstudyguide.md#hooked-on-state) as a reference to complete this exercise.  It contains some of the more salient points taken from the React docs.  Read our hints below as well to help you with this exercise.

Also note that you will not have to modify any other components - just `TodoApp` and `AddTodo`, and that's it!

Once you complete this milestone, you should appreciate the simplicity of hooks. We will not get into more advanced React patterns, but rest assured that hooks will continue to enrich your life with their power and expressiveness.


**Hints** (click the arrow to reveal)
<details markdown="1">
  <summary>Remember, hooks have a specific restriction.</summary>
  Hooks don't work with class based components -- make sure to refactor to a functional component.
</details>
<details markdown="1">
  <summary>How is state initialized?</summary>
  There will be no constructor, so state is initialized in the call to `useState`.
</details>
<details markdown="1">
  <summary>How do hooks affect the existing methods?</summary>
  These can still be used to update the state -- just refactor the methods from the class as helper functions.
</details>  


## Milestone 10: Styling our components
Our app works great, but it doesn’t look great. Let’s use [CSS Modules](https://github.com/css-modules/css-modules) to make our interface a little bit easier to use and understand. We can use a CSS framework [Milligram]("https://milligram.io/"), along with some of our own styling rules to prettify our to-do app.

First install Milligram
```bash
$ npm install milligram
```

Next create a new file `src/todos.module.css` and fill it with some very basic, but noticeable CSS.

```css
.addTodos {
  background: red;
}
```

Then in `add-todo.jsx` import the css module.

```jsx
import styles from './todos.module.css';
```
CSS Modules allow you to assign your custom styles to a component within the JSX by specifying the className you’d like to assign to that component. When Webpack imports the CSS file it produces a Javascript object that maps the class name you defined in the CSS to a unique hash. This virtually guarantees there will be no style conflicts in your app since all of the hashes are namespaced by file. Add the following attribute to the button tag.

```jsx
<button className={styles['addTodos']} onClick={this.handleSubmit}>
```

Refresh the page and confirm that your add todo button is now a horrific red. The CSS Module works and you can inspect the button to see the hash that was generated. But nobody is going to want to click that! Instead, let’s use Milligram’s `button-outline`. First, lets import Milligram as global styles. Go to `index.js` and add

```js
import 'milligram';
```

Milligram will be available as global styles so you can apply class names to your jsx to use them. For example back in `add-todo.jsx` replace the className you just added with:

```jsx
<button className="button button-outline">
```

Now your button should look a lot more button-y. Notice that for Milligram we aren’t using CSS Modules. Create React App uses the `[name].module.css` file name convention to process CSS as Modules. Otherwise it is loaded as a regular stylesheet.

Take this time to mix in some basic Milligram boilerplate CSS with some of your own custom CSS. Add your custom css to `todos.module.css` and use the original pattern we used when we made the button red. If you are using Milligram styles, just add the appropriate classes. Here are a couple of suggestions:
- Make the add todos textbox a bit more prominent. This should be a focal point of your app.
- Make the delete todo button more intimidating. Users should be fully aware of the consequences of clicking it just by looking at it.
- Try to use some of the extra white space on the screen.
- Refactor the markup as needed

# Lab 2

In this lab, we will refactor our Todo List app from Lab 1.  Go ahead and start from your finished version of lab 1.

This app will have the same functionality as the previous lab; although there are some stretch goals to give you a chance to flex your React and Redux muscles. Today's lab will focus on integrating Redux, so that our todos are no longer stored in component state, but rather in a centralized store. There are required milestones in this lab that should be feasible to get through in the time allotted as well as a bonus milestones you are encouraged to attempt in class if you finish early or later on your own. If you are stuck at any point don't hesitate to ask for assistance. This lab may be challenging as we will be introducing new vocabulary and patterns.


#### Required concepts before starting:
* Javascript - [ES6](https://github.com/varoonsahgal/react-fundamentals/blob/main/es6studyguide.md)
* [React - components, classes, props, JSX](https://github.com/varoonsahgal/react-fundamentals/blob/main/reactstudyguide.md)

> If any of these concepts above need a refresher, please follow the links before getting started with the lab.
sdfsd
#### What you will learn:
* **React** - passing props, using map, further understanding of components.
* **Redux** - store, reducers, mapStateToProps, connect. We will refer to Redux QuickStart Guide

#### Why we are doing this lab:
Maintaining state on the front-end is a requirement for any apps that purport to do something of interest. Redux is a powerful new paradigm for managing state in a performant, functional, and maintainable way. The learning curve can be steep because it has it own vocabulary and design patterns. React and Redux are now essential parts of the front-end toolbelt for tech companies around the world. Notable ones being Facebook, Airbnb, Reddit, Netflix, Walmart, and of course Salesforce!


## Milestone 1: Create a Reducer
Redux's `createStore` function requires a root reducer to construct a store with. This reducer can be composed of many reducers, each managing their own branch of the state tree. However in our simple app, we only have one piece of state to track: todos. We will create a reducer to manage our collection of todos.

First, let's add Redux and the bindings for React to our project:

```bash
$ npm install redux react-redux
```
Create a file `reducer.js` in the `src` directory. A reducer must return the current state if it doesn't recognize an action type, and it must also provide an initial state if the current state is undefined. We'll begin with a reducer that does this absolute minimum before augmenting it with the ability to add and remove todos.

```js
export const todos = (state = [], action) => {
  switch (action.type) {
    default:
      return state;
  }
};
```


## Milestone 2: Create the Store
In `src/index.js` import the `createStore` function, the `Provider` higher order component as well as the root reducer you just created:

```jsx
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { todos } from './reducer';
```

Now let's make our Redux store. Before the `ReactDOM.render` invocation, add:
```jsx
const store = createStore(todos);
```

Remember, this is all that's required to initalize a Redux store. However, since an empty todos array is not very interesting to look at, let's take advantage of `createStore`'s optional second argument – inital state. Right above our store initialization add these sample todos (or feel free to invent your own):

```jsx
const initialTodos = [
  { id: 1, text: 'use redux in todo app' },
  { id: 2, text: 'complete bonus milestone' },
]
```

And pass the array as the second argument to `createStore`

```jsx
const store = createStore(todos, initialTodos);
```

Now when we wire up our app with the redux store we'll get some visual feedback of our success! Ok, we need to make the store available to our component tree. Just after your `store` code, create an `App` component that wraps `TodoApp` with the `Provider` we importer earlier. Then pass your Redux store as a prop to the `Provider`, which will make any component in the hierarchy able to connect to the redux store using `connect`.

```jsx
const App = () => (
  <Provider store={store}>
    <TodoApp />
  </Provider>
);
```

Finally, let's render our provider-wrapped app:

```jsx
ReactDOM.render(<App />, document.getElementById('root'));
```

> It's common to inline the provider-wrapped app directly in the `render` method:
>
> ```javascript
> ReactDOM.render(
>   <Provider store={store}>
>     <TodoApp />
>   </Provider>, 
>   document.getElementById('root')
> );
> ```


## Milestone 2.5: Remove React State
In `src/todo-app.jsx` let's remove the old component level state.  If you are using hooks in your code, then just comment out the call to `useState`, and the calls to your state updater function.  

If you are not using hooks for component level state, then you can just comment out your state initialization code in your component class. 

Make sure to also remove the `todos` prop being passed to `TodoList`.

At this point you'll be getting errors, because we no longer have a todos array available in `TodoList`, so let's remedy that.


## Milestone 3: Access Redux State

The `react-redux` bindings library provides the `connect` function to hook up any component to the Redux store. This allows it to access state and dispatch actions to update the state. Let's `connect` `TodoList` to the store.

The `connect` function has an interesting function signature. The first argument should be a function that will receive the current state as an argument. It should return an object with key value pairs that will be passed to the connected component as props. The function is commonly called `mapStateToProps` since this name describes exactly what it does, but the actual variable name is not important. This function is where you can select the branches of the state tree your component is interested in and it will directly receive them as props – no matter how deeply nested it is. No more passing props down the component tree!

In our app, remember that our redux state is simply an array of todos, something like:

```javascript
[{ id: 1, text: 'todo1' }, { id: 2, text: 'todo2' }]
```

So, when we pass the todos down, we can just pass the entire state. In more complex apps, you will only be passing in a "slice" of the state, but we'll talk more about that later.

Let's get to work. In `src/todo-list.jsx` add the following function definition after the component:

```jsx
const mapStateToProps = (state) => {
  return {
    todos: state
  }
};
```

and now import `connect`

```jsx
import { connect } from 'react-redux';
```

and modify the export statement

```jsx
export default connect(mapStateToProps)(TodoList);
```

Take a moment to study how we use `connect` – it accepts a state-mapping function, returns a new function that accepts a React component, and that second function returns a new connected component that wraps ours and is responsible for passing it the props we specified in the mapper. (This pattern is called a "higher order component.") The connected wrapper component is subscribed to updates from the store and will rerender when state changes, passing the new values as props to our wrapped component through `mapStateToProps`.

You should now be able to see our new list of todos rendering on the page. Take a moment to inspect the page with the React dev tools. If you don't have them installed, [get them here](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en-US). To open the React dev tools once installed, open the regular Chrome dev tools and navigate to the new tab called `React`.

You should be able to inspect the component hierarchy. Try to locate the component created by connect to provide the props to `TodoList`.


## Milestone 4: Update State - Add Todo

In order to update state, we need an action object that can be given to the dispatch, which then sends it to reducer which updates the state. Typically we write action creators to return different types of action objects, so we keep our code DRY. 

Create a file `src/actions.js` and add the action creator:

```jsx
export const addTodo = text => ({ type: 'ADD_TODO', text })
```

Remember that the Redux store does not allow direct access to the state. In order to update state you must `dispatch` an action describing how the state should change and have a reducer implemented to respond to that action by producing the new state. Actions are POJOs (plain old javascript objects) whose only requirement is a `type` key. The redux store provides the `dispatch` method, but we'll use the `react-redux` bindings to expose it to our components just like we did to expose state.

Let's refactor the add todo logic in `src/AddTodo.jsx` to dispatch an action to the Redux store. First we'll need to import our helper funtion:

```jsx
import { connect } from 'react-redux';
import { addTodo } from './actions';
```

Notice the that the action creator makes the todo and assigns it to the payload property. We'll use this to make our todos instead of the logic in the `handleSubmit` method. However, we need to dispatch the action to the store. So, next we'll use the action creator in our `mapDispatchToProps` function. Add the following right after the action creator:

```jsx
const mapDispatchToProps = (dispatch) => {
  return {
    handleAdd: text => dispatch(addTodo(text))
  }
};
```

This function is analogous to `mapStateToProps`: it will receive the store's dispatch method as an argument, and it is expected to return an object of key value pairs that will be passed to the component as props. Here our values are functions that invoke the `dispatch` method with an action.

At the top of your AddTodo component (outside of any function) be sure to grab state from the useState hook like so:

```jsx
 const[todoText, setTodoText] = useState('');
```

Now let's use the dispatcher in the component. Refactor the `handleSubmit` method as follows:

```jsx
 const handleSubmit = (e) => {
    e.preventDefault()
    let text = todoText.trim()
    if (!text) return
    handleAdd(text)
    setTodoText('')
  }
```

Our last step is to wire up the component with `connect`, which means a quick refactor of the export statement.

```jsx
export default connect(null, mapDispatchToProps)(AddTodo);
```

Take particular notice here that the first argument to `connect` is `null`. Why might this be the case? What did we previously pass as the first argument?

Since `AddTodo` doesn't need to access the current state, we don't need to provide a `mapStateToProps` function, but position is important and `mapDispatchToProps` must be the second argument, so we pass the `null` placeholder as our first argument.

Now that `handleAdd` is provided to our component as a prop by `connect` let's go back to `src/todo-app.jsx` and clean up the code we no longer need. `AddTodo` no longer requires `handleAdd` to be passed as a prop by `TodoApp` and naturally `addTodo` is no longer used and can also be removed.

> It is common to provide a `mapStateToProps` function, even if it returns an empty object:
> 
> ```javascript
> const mapStateToProps = (state, ownProps) => ({})
> ```
> 
> This allows the signature at the bottom to be consistent, and you don't have to keep track of whether a `null` is being passed or not.

If, in a frenzy of uncontrolled excitement, you fired up your app and tried adding a todo, you may have been disappointed to see nothing happen. Although we are currently dispatching an action, there is a second piece required to update the state. The reducer must be explicitly written to handle the action type you are dispatching, so our work is not yet done.

In `src/reducer.js` we'll now make our `todos` reducer actually do something interesting instead of just returning the current state. The action type we used in the action creator was `ADD_TODO` so we'll need to support updating the state in that case.

Before you rush into implementation, let's write some tests! TDD is easy to do with Redux and testing your business logic hugely improves the codebase. `create-react-app` provides the `Jest` testing framework out of the box; all you have to do is put a `whatever.test.js` file somewhere and then when you run `yarn test` it will pick it up!

Industry practice is to collocate test files alongside their implementation, bundled together under a `__tests__` folder. So let's create a file `src/__tests__/reducer.test.js` file.

```javascript
import { todos } from '../reducer'
import { addTodo } from '../actions'

describe('src.reducer', () => {
  describe('ADD_TODO', () => {
    beforeAll(() => {
      jest.spyOn(Date, 'now').mockImplementation(() => 1234567890)
    })
    
    it('should add a new todo to an empty list', () => {
      const state = []
      const newState = todos(state, addTodo('TDD is awesome'))
      expect(newState).toEqual([ {id: 1234567890, text: 'TDD is awesome'} ])
    })

    it('should add a new todo at the end of the list', () => {
      const state = [{ id: 1, text: 'TDD is awesome' }]
      const newState = todos(state, addTodo('Remember to check all the cases!'))
      expect(newState).toEqual([
        { id: 1, text: 'TDD is awesome' },
        { id: 1234567890, text: 'Remember to check all the cases!' }
      ])
    })
  })
})
```

Once you have tests that fail, write the implementation to make them pass!

```js
export const todos = (state = [], action) => {
  switch (action.type) {
    case 'ADD_TODO':
      return [...state, { id: Date.now(), text: action.text }];
    default:
      return state;
  }
};
```

When this reducer is invoked with an action of type `ADD_TODO` it will **create a new array** with all the current todos and append the payload, ie. the new todo. Remember the reducer must be implemented as a pure function meaning **you cannot mutate the existing array.**

Test your todo app. The list should now update as you add todos!


## Milestone 5: Update State - Delete Todo

Now that you've seen the Redux pattern, it's your turn to try it out. Refactor `TodoList` to delete todos from the Redux store.

You'll need to:

- Define an action type for deleting todos
- Make an action creator or don't – you choose
- Provide a mechanism for your component to dispatch an action of the type you defined
- Enable the store to recognize that type of action
- This isn't X-Men so remember, NO MUTATIONS
  - <details markdown="1">
      <summary>HINT: Not sure how to immutably remove an item from a list?</summary>
      Try using `Array#filter` to create a new array where it only has certain todos... what would be a way to filter out the todo in question?
    </details>
- Clean up any code that has been made superfluous
- If you are stuck at any point, please ask a question! We're happy to point you in the right direction!

## Milestone 6: Refactor MDTP

Learning how `mapDispatchToProps` worked by spelling out the functions was great, but it's time to stop typing so much. Try out refactoring the MDTP using the "object shorthand" and pass in the action creators values. Read more [here](https://react-redux.js.org/using-react-redux/connect-mapdispatch#defining-mapdispatchtoprops-as-an-object).

Typically, you use the same prop name as the action creator name. You'll want to rename `handleAdd` to be `addTodo` and then return a MDTP such as:

```javascript
const mapDispatchToProps = { addTodo }
```

## Milestone 7: Access `dispatch` Directly

You can also try passing nothing in for the second argument of `connect` in order to have `dispatch` passed as a prop to your component. Read more [here](https://react-redux.js.org/using-react-redux/connect-mapdispatch#default-dispatch-as-a-prop). Then you can invoke it directly with the action creator, something like:

```javascript
this.props.dispatch(addTodo(text))
```

Think about the strengths and weaknesses of the three approaches: defining MDTP as a function, defining it as an object, and having `dispatch` injected, and talk about them with a coworker. Which style do you prefer, and why?

`<opinion>`In most cases, it has been our experience that accessing `dispatch` directly is the best pattern to follow -- it's still clear what is a Redux action, and it leads to the least amount of boilerplate (it only gets worse when you add Flow or TypeScript on top). There are only a few cases where using the MDTP pattern is useful in creating certain advanced React patterns, and they're quite limited (we've used them in maybe 0.1% of our components).`</opinion>`

## Bonus: [Feature] “Complete” Todos

It would be neat if a user could add todos and mark them as completed in addition to deleting them. To toggle the state of the todo, the user should click on the todo text itself. You'll have to modify our current data model to track this new information. You also have lots of creative freedom in developing the UI. A more straight-forward implementaion could display the existing todo list and add styling to identify completed todos – strikethrough is a reasonable choice. Feeling fancy? Provide a visibility toggle so the user can view pending, completed, or all todos. A more complex implementation might render two separate lists, one for pending and one for completed. This is a great way to leverage the reusability of React components. Don't be limited by our suggestions! You could also try out keeping track of how many todos the user has marked completed in the current session with a counter.

You'll notice that `todos` only keeps track of the current todos state. If you add things like a visiblity filter, you'll want to store that in a separate "slice" or namespace of the state, e.g. `visibilityFilter`. You'll want to read up on [combineReducers](https://redux.js.org/api/combinereducers) to make it happen.
