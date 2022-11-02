import React from 'react';
import './App.css';
import Navbar from './components/Navbar/index';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/about';
import Blogs from './pages/blogs';
import SignUp from './pages/signup';
import Contact from './pages/contact';

function App() {
return (
	<Router>
	<Navbar />
	<Routes>
		<Route path='/' exact element={<Home />} />
		<Route path='/about' element={<About/>} />
		<Route path='/contact' element={<Contact/>} />
		<Route path='/blogs' element={<Blogs/>} />
		<Route path='/sign-up' element={<SignUp/>} />
	</Routes>
	</Router>
);
}

export default App;


// import React from "react";
// // import { Link } from 'react-router-dom'

// class App extends React.Component{
//   constructor(){
//     super();
//     this.state={
//       data:[]
//     }
//   }

// fetchdata(){
//   fetch('http://localhost:8000/api/categories')
//   .then(response=>response.json())
//   .then((data)=>{
//     this.setState({data:data});
//   });
//   // console.log(data)
// }

// componentDidMount(){
//   this.fetchdata();
// }

//   render(){
//     const catdata =this.state.data;
//     const rows = catdata.map((categ)=>
//       <tr key={categ.id}>
//         <td>{categ.name}</td>
//       </tr>
//     )
//     return(
//       <table className="table ">
//         <thead>
//           <tr>
//             <th>
//               Name is
//             </th>
//           </tr>
//         </thead>
//         <tbody>
//           {rows}
          
//         </tbody>
//         </table>
//           // <br/>
//           // <tr>inside table body in return statment!!!!!</tr>
      
//     );
//   }
// }


// export default App

// import React, { Component } from "react"

// class App extends Component {
  
//   constructor(props) {
    
//     super(props);
//     this.state = {
//       viewCompleted: false,
//       activeItem: {
//         catname: "",
//         completed: false
//       },
//       catList: []
//       };
//   }

//   async componentDidMount() {
//     try {
//       <h1>Error in Catch Block!!!</h1>

//       const res = await fetch('http://localhost:8000/api/category/');
//       const catList = await res.json();
//       this.setState({
//         catList
//       });
//     } catch (e) {
//       console.log(e);
//   }
//   }
//   renderItems = () => {
//     <h1>renderitem</h1>
//     const { viewCompleted } = this.state;
//     const newItems = this.state.catList.filter(
//       item => item.completed === viewCompleted
//     );
//     return newItems.map(item => (
      
//       <li 
//         key={item.id}
//         className="list-group-item d-flex justify-content-between align-items-center"
//       >
//         <span 
//           className={`todo-title mr-2 ${
//             this.state.viewCompleted ? "completed-todo" : " not completed!!!!"
//           }`}
//           catname={item.name}
//           >
//                     <h1>mapfunction</h1>

//             {item.name}
//           </span>
//       </li>
//     ));
//   };

//  render(){
//   return (
//     <main className="content">
//     <div className="row">
//       <div className="col-md-6 col-sm-10 mx-auto p-0">
//         <div className="card p-3">
//           <ul className="list-group list-group-flush">
//             {this.renderItems()}
//             <h1>Render Body</h1>
//           </ul>
//         </div>
//       </div>
//     </div>
//   </main>
//   )
       
//  }
// }
// export default App


// =========================================================
// ==========================================================


// import React, { Component } from "react"

// const todoItems = [
//   {
//     id: 1,
//     title: "Nature walk in the park",
//     description: "Visit the park with my friends",
//     completed: true
//   },

//   {
//     id: 2,
//     title: "Visit",
//     description: "Got to my aunt's place",
//     completed: true
//   },

//   {
//     id: 3,
//     title: "Write",
//     description: "Do an article about anthropology",
//     completed: true
//   },
// ];

// class App extends Component {
//     constructor(props) {
//       super(props);
//       this.state = {todoItems};
//     };

//     render() {
//       return (
//         <main className="content">
//         <div className="row">
//           <div className="col-md-6 col-sm-10 mx-auto p-0">
//             <div className="card p-3">
//               <ul className="list-group list-group-flush">
//               {this.state.todoItems.map(item => (
//               <div>
//                 <h1>{item.title}</h1>
//                 <span>{item.description}</span>
//               </div>
//               ))}
//               </ul>
//             </div>
//           </div>
//         </div>
//       </main>
//       )
//     }
//   }
  
// export default App;


// =================================================?
// import React, { Component } from "react";
// import Modal from "./components/Modal";
// import axios from "axios";

// class App extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       viewCompleted: false,
//       todoList: [],
//       modal: false,
//       activeItem: {
//         title: "",
//         description: "",
//         completed: false,
//       },
//     };
//   }

//   componentDidMount() {
//     this.refreshList();
//   }

//   refreshList = () => {
//     axios
//       .get("/api/todos/")
//       .then((res) => this.setState({ todoList: res.data }))
//       .catch((err) => console.log(err));
//   };

//   toggle = () => {
//     this.setState({ modal: !this.state.modal });
//   };

//   handleSubmit = (item) => {
//     this.toggle();

//     if (item.id) {
//       axios
//         .put(`/api/todos/${item.id}/`, item)
//         .then((res) => this.refreshList());
//       return;
//     }
//     axios
//       .post("/api/todos/", item)
//       .then((res) => this.refreshList());
//   };

//   handleDelete = (item) => {
//     axios
//       .delete(`/api/todos/${item.id}/`)
//       .then((res) => this.refreshList());
//   };

//   createItem = () => {
//     const item = { title: "", description: "", completed: false };

//     this.setState({ activeItem: item, modal: !this.state.modal });
//   };

//   editItem = (item) => {
//     this.setState({ activeItem: item, modal: !this.state.modal });
//   };

//   displayCompleted = (status) => {
//     if (status) {
//       return this.setState({ viewCompleted: true });
//     }

//     return this.setState({ viewCompleted: false });
//   };

//   renderTabList = () => {
//     return (
//       <div className="nav nav-tabs">
//         <span
//           onClick={() => this.displayCompleted(true)}
//           className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
//         >
//           Complete
//         </span>
//         <span
//           onClick={() => this.displayCompleted(false)}
//           className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
//         >
//           Incomplete
//         </span>
//       </div>
//     );
//   };

//   renderItems = () => {
//     const { viewCompleted } = this.state;
//     const newItems = this.state.todoList.filter(
//       (item) => item.completed === viewCompleted
//     );

//     return newItems.map((item) => (
//       <li
//         key={item.id}
//         className="list-group-item d-flex justify-content-between align-items-center"
//       >
//         <span
//           className={`todo-title mr-2 ${
//             this.state.viewCompleted ? "completed-todo" : ""
//           }`}
//           title={item.description}
//         >
//           {item.title}
//         </span>
//         <span>
//           <button
//             className="btn btn-secondary mr-2"
//             onClick={() => this.editItem(item)}
//           >
//             Edit
//           </button>
//           <button
//             className="btn btn-danger"
//             onClick={() => this.handleDelete(item)}
//           >
//             Delete
//           </button>
//         </span>
//       </li>
//     ));
//   };

//   render() {
//     return (
//       <main className="container">
//         <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
//         <div className="row">
//           <div className="col-md-6 col-sm-10 mx-auto p-0">
//             <div className="card p-3">
//               <div className="mb-4">
//                 <button
//                   className="btn btn-primary"
//                   onClick={this.createItem}
//                 >
//                   Add task
//                 </button>
//               </div>
//               {this.renderTabList()}
//               <ul className="list-group list-group-flush border-top-0">
//                 {this.renderItems()}
//               </ul>
//             </div>
//           </div>
//         </div>
//         {this.state.modal ? (
//           <Modal
//             activeItem={this.state.activeItem}
//             toggle={this.toggle}
//             onSave={this.handleSubmit}
//           />
//         ) : null}
//       </main>
//     );
//   }
// }

// export default App;