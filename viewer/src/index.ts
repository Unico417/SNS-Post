import React from "react";
import ReactDOM from "react-dom/client";
import UserInterface from "./Component/UserInterface";

ReactDOM.createRoot(document.querySelector('#main')!)
    .render(React.createElement(UserInterface, {}));
console.log('Hello World!');
