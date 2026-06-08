const API_BASE_URL = "http://127.0.0.1:8000";

export async function getAIUpdates() {
  const response = await fetch(`${API_BASE_URL}/ai-updates`);

  if (!response.ok) {
    throw new Error("Failed to fetch AI updates");
  }

  return response.json();
}

export async function getAISummits() {
  const response = await fetch(`${API_BASE_URL}/ai-summits`);

  if (!response.ok) {
    throw new Error("Failed to fetch AI summits");
  }

  return response.json();
}