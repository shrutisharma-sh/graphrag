import { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import axios from "axios";

export default function App() {

  const [query, setQuery] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const getBestPipeline = () => {

    if (!result) return null;

    const scores = [
      {
        name: "llm_only",
        score: result.llm_only.evaluation.f1_score
      },

      {
        name: "basic_rag",
        score: result.basic_rag.evaluation.f1_score
      },

      {
        name: "graph_rag",
        score: result.graph_rag.evaluation.f1_score
      }
    ];

    scores.sort((a, b) => b.score - a.score);

    return scores[0].name;
  };


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
  const bestPipeline = getBestPipeline();

  const chartData = result ? [

    {
      name: "LLM",
      latency: result.llm_only.latency_seconds,
      tokens: result.llm_only.output_tokens_estimate,
      cost: result.llm_only.estimated_cost_usd,
      f1: result.llm_only.evaluation.f1_score
    },

    {
      name: "Basic RAG",
      latency: result.basic_rag.latency_seconds,
      tokens: result.basic_rag.output_tokens_estimate,
      cost: result.basic_rag.estimated_cost_usd,
      f1: result.basic_rag.evaluation.f1_score
    },

    {
      name: "GraphRAG",
      latency: result.graph_rag.latency_seconds,
      tokens: result.graph_rag.output_tokens_estimate,
      cost: result.graph_rag.estimated_cost_usd,
      f1: result.graph_rag.evaluation.f1_score
    }

  ] : [];

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



        <>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">


            {/* //llm  */}

            <div className={`p-5 rounded shadow ${bestPipeline === "llm_only"
              ? "bg-green-100 border-2 border-green-500"
              : "bg-white"}`}>

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

              <p>
                BERTScore F1:
                {" "}
                {result.llm_only.evaluation.f1_score}
              </p>

            </div>


            {/* //rag  */}



            <div className={`p-5 rounded shadow ${bestPipeline === "basic_rag"
              ? "bg-green-100 border-2 border-green-500"
              : "bg-white"}`}>

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

              <p>
                BERTScore F1:
                {" "}
                {result.basic_rag.evaluation.f1_score}
              </p>

            </div>



            {/* //graphrag */}
            <div className={`p-5 rounded shadow ${bestPipeline === "graph_rag"
              ? "bg-green-100 border-2 border-green-500"
              : "bg-white"}`}>

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

              <p>
                BERTScore F1:
                {" "}
                {result.graph_rag.evaluation.f1_score}
              </p>
            </div>

          </div>
          // chart section

          <div className="mt-10 bg-white p-6 rounded shadow">

            <h2 className="text-3xl font-bold mb-6">
              Latency Comparison
            </h2>

            <div className="h-80">

              <ResponsiveContainer width="100%" height="100%">

                <BarChart data={chartData}>

                  <XAxis dataKey="name" />

                  <YAxis />

                  <Tooltip />

                  <Bar dataKey="latency" />

                </BarChart>

              </ResponsiveContainer>

            </div>

          </div>

          <div className="mt-10 bg-white p-6 rounded shadow">

            <h2 className="text-3xl font-bold mb-6">
              Token Usage Comparison
            </h2>

            <div className="h-80">

              <ResponsiveContainer width="100%" height="100%">

                <BarChart data={chartData}>

                  <XAxis dataKey="name" />

                  <YAxis />

                  <Tooltip />

                  <Bar dataKey="tokens" />

                </BarChart>

              </ResponsiveContainer>

            </div>

          </div>

          <div className="mt-10 bg-white p-6 rounded shadow">

            <h2 className="text-3xl font-bold mb-6">
              Cost Comparison
            </h2>

            <div className="h-80">

              <ResponsiveContainer width="100%" height="100%">

                <BarChart data={chartData}>

                  <XAxis dataKey="name" />

                  <YAxis />

                  <Tooltip />

                  <Bar dataKey="cost" />

                </BarChart>

              </ResponsiveContainer>

            </div>

          </div>
          <div className="mt-10 bg-white p-6 rounded shadow">

            <h2 className="text-3xl font-bold mb-6">
              Benchmark Charts
            </h2>

            <div className="h-80">

              <ResponsiveContainer width="100%" height="100%">

                <BarChart data={chartData}>

                  <XAxis dataKey="name" />

                  <YAxis />

                  <Tooltip />

                  <Bar dataKey="f1" />

                </BarChart>

              </ResponsiveContainer>

            </div>

          </div>
        </>


      )}

    </div>
  );
}