import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import HomePage from "./pages/HomePage";
import MainLayout from "./layouts/MainLayout";
import GameHub from "./pages/GameHub";
import axios from "axios";
import GameLobby from "./pages/GameLobby";
import Tracker from "./pages/Tracker";

axios.defaults.baseURL = "http://127.0.0.1:5000/api/v1/";
axios.defaults.withCredentials = true;

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      // <Route path="/" element={<MainLayout />}>
      <>
        <Route path="/" element={<HomePage />} />
        <Route path="/gamehub" element={<GameHub />} />
        <Route path="/gamelobby" element={<GameLobby />} />
        <Route path="/tracker" element={<Tracker />} />
      </>
      // </Route>
    )
  );

  return <RouterProvider router={router} />;
}

export default App;
