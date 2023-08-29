import React from "react";

// Functional Components: These types of components have no state of their own and only contain render methods, and therefore are also called stateless components. They may derive data from other components as props (properties).

const FunctionalComponent = (props) => {
  return <h1>Hello Functional Component {props.funcComp}</h1>;
};

export default FunctionalComponent;
