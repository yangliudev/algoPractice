import React, { useState } from "react";

import FunctionalComponent from "./components/FunctionalComponent";
import ClassComponent from "./components/ClassComponent";
import "./App.css";

function App() {
  const [counter, setCounter] = useState(0);

  const addCounter = () => {
    setCounter(counter + 1);
  };

  const minusCounter = () => {
    setCounter(counter - 1);
  };

  return (
    <div className="App">
      <button onClick={() => addCounter()}>+</button>
      <h1>{counter}</h1>
      <button onClick={() => minusCounter()}>-</button>

      <FunctionalComponent funcComp="props one" />
      <ClassComponent classComp="props two" />
    </div>
  );
}

export default App;
