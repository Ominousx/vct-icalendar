const GITHUB_API_URL =
  "https://api.github.com/repos/Ominousx/vct-icalendar/commits";

async function fetchLastUpdate() {
  try {
    const response = await fetch(GITHUB_API_URL);
    const data = await response.json();
    if (data && data.length > 0) {
      const lastCommitDate = new Date(data[0].commit.committer.date);
      document.getElementById("update-date").textContent =
        lastCommitDate.toDateString();
    } else {
      document.getElementById("update-date").textContent = "Unable to fetch";
    }
  } catch (error) {
    console.error("Error fetching update date:", error);
    document.getElementById("update-date").textContent = "Error fetching";
  }
}

fetchLastUpdate();
