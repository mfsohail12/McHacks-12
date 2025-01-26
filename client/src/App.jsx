import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import HomePage from "./pages/HomePage";
import MainLayout from "./layouts/MainLayout";
import GameHub from "./pages/GameHub";

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      // <Route path="/" element={<MainLayout />}>
      <>
        <Route path="/" element={<HomePage />} />
        <Route path="/gamehub" element={<GameHub />} />
      </>
      // </Route>
    )
  );

  return <RouterProvider router={router} />;
}

export default App;
