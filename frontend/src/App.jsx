import { useState } from "react";
import axios from "axios";

export default function App() {

  const [query, setQuery] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);


  const handleCompare = async () => {

    if (!query) return;

    setLoading(true);

    try {

      const response = await axios.get(
        `http://127.0.0.1:8000/compare?query=${query}`
      );

      setResult(response.data);
      console.log(response.data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold mb-6">
        GraphRAG Benchmark Dashboard
      </h1>


      <div className="flex gap-4 mb-8">

        <input
          type="text"
          placeholder="Ask something..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 p-3 rounded border"
        />

        <button
          onClick={handleCompare}
          className="bg-black text-white px-6 rounded"
        >
          Compare
        </button>

      </div>


      {loading && (
        <p className="text-lg">Running pipelines...</p>
      )}


      {result && (

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">


          {/* //llm  */}

          <div className="bg-white p-5 rounded shadow">

            <h2 className="text-2xl font-bold mb-4">
              LLM Only
            </h2>

            <p className="mb-4">
              {result.llm_only.response}
            </p>

            <p>
              Latency:
              {" "}
              {result.llm_only.latency_seconds}s
            </p>

            <p>
              Tokens:
              {" "}
              {result.llm_only.output_tokens_estimate}
            </p>

            <p>
              Cost:
              {" "}
              ${result.llm_only.estimated_cost_usd}
            </p>

          </div>


          {/* //rag  */}



          <div className="bg-white p-5 rounded shadow">

            <h2 className="text-2xl font-bold mb-4">
              Basic RAG
            </h2>

            <p className="mb-4">
              {result.basic_rag.response}
            </p>

            <p>
              Latency:
              {" "}
              {result.basic_rag.latency_seconds}s
            </p>

            <p>
              Tokens:
              {" "}
              {result.basic_rag.output_tokens_estimate}
            </p>

            <p>
              Cost:
              {" "}
              ${result.basic_rag.estimated_cost_usd}
            </p>

          </div>



          {/* //graphrag */}
          <div className="bg-white p-5 rounded shadow">

            <h2 className="text-2xl font-bold mb-4">
              GraphRAG
            </h2>

            <p className="mb-4">
              {result.graph_rag.response}
            </p>

            <p>
              Latency:
              {" "}
              {result.graph_rag.latency_seconds}s
            </p>

            <p>
              Tokens:
              {" "}
              {result.graph_rag.output_tokens_estimate}
            </p>
            <p>
              Cost:
              {" "}
              ${result.graph_rag.estimated_cost_usd}
            </p>
          </div>

        </div>
      )}

    </div>
  );
}