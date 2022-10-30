
import { render } from "react-dom";

import React from 'react'

const App = () => {
  return (
    <div>this is the first app from react </div>
  )
}

export default App

const appDiv = document.getElementById("app");
render(<App />, appDiv);