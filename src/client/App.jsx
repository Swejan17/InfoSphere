import Content from "./Content";
import Home from "./Home";
import { Routes, Route } from "react-router-dom";


export default function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/search" element={<Home />} />
            <Route path="/content/:id" element={<Content />} />
            <Route path="*" element={<Home />} />
        </Routes>
    )
}