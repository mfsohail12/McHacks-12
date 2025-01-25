import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import HomePage from "./components/HomePage";

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(<Route path="/home" element={<HomePage />} />)
  );

  return <RouterProvider router={router} />;
}

export default App;
