import React from "react";

// Class Components: These types of components can hold and manage their own state and have a separate render method to return JSX on the screen. They are also called Stateful components as they can have a state.

class ClassComponent extends React.Component {
  render() {
    return <h1>Hello Class Component {this.props.classComp}</h1>;
  }
}

export default ClassComponent;
