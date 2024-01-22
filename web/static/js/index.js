_go_with_disabled_exit = (target) => {
  exit_disable = true;
  location.assign(target);
  exit_disable = false;
};

link_api = () => {
  _go_with_disabled_exit("/api/ui/");
};

fetch_measurements = async () => {
  const response = await fetch("/api/measurements", { method: "GET" });
  const json = await response.json();

  const list = document.createDocumentFragment();
  json.map((measurement) => {
    const measurementItem = `
        <div class="col card m-1 border-primary">
            <div class="card-header">${measurement.name}</div>
            <div class="card-body">
                <span class="card-title badge bg-primary">${measurement.value}</span>
                <span class="card-text badge bg-secondary">${measurement.timestamp}</span>
            </div>
        </div>
        `;
    const item = document.createElement("div");
    item.innerHTML = measurementItem;
    list.appendChild(item);
  });

  const contentItem = document.getElementById("measurement-content");
  contentItem.appendChild(list);
};
