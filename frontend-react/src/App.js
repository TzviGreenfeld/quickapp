import logo from "./logo.svg";
import "./App.css";
import UserComponent from "./components/Users";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <UserComponent />
      </header>
    </div>
  );
}

export default App;
