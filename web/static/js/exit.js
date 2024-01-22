var exit_disable = false;
const exit = async function () {
  if (!exit_disable) {
    const response = await fetch("/api/exit", { method: "POST" });
    console.log("status", response.statusText, response.status);
    return "do you really want to exit?";
  }
  return null;
};
window.addEventListener("beforeunload", exit);
