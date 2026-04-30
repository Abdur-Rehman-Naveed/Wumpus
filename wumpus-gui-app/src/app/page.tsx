"use client"; // This tells Next.js this is an interactive page
import { useState } from "react";

export default function WumpusGame() {
  // 1. State: This keeps track of the message from Python
  const [message, setMessage] = useState("Click a cell to check logic");

  // 2. The Bridge Function: This talks to Python
  async function checkCell(x: number, y: number) {
    const response = await fetch(`http://localhost:8000/api/logic?x=${x}&y=${y}`);
    const data = await response.json();
    setMessage(data.msg); // Update the screen with Python's answer
  }

  // 3. The UI: This is what you see
  return (
    <div className="p-10 flex flex-col items-center gap-6">
      <h1 className="text-3xl font-bold">Wumpus World</h1>
      <p className="bg-gray-100 p-4 rounded">{message}</p>

      {/* A simple 2x2 grid for now to keep it easy */}
      <div className="grid grid-cols-2 gap-2">
        <button className="w-20 h-20 bg-blue-500 text-white" onClick={() => checkCell(0, 0)}>0,0</button>
        <button className="w-20 h-20 bg-blue-500 text-white" onClick={() => checkCell(0, 1)}>0,1</button>
        <button className="w-20 h-20 bg-blue-500 text-white" onClick={() => checkCell(1, 0)}>1,0</button>
        <button className="w-20 h-20 bg-blue-500 text-white" onClick={() => checkCell(1, 1)}>1,1</button>
      </div>
    </div>
  );
}