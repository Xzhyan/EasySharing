// PopUp de Mensagens
function hideMsgPopUp() {
  const messages = document.querySelectorAll(".msg-pop-up");

  if (!messages.length) return;

  messages.forEach((msg) => {
    setTimeout(() => {
      msg.style.opacity = "0";

      setTimeout(() => {
        msg.remove();
      }, 500);
    }, 3000);
  });
}
document.addEventListener("DOMContentLoaded", hideMsgPopUp);

// Selecionar todos, desmarcar todos
function selectAllCheckBox() {
  const selectAll = document.getElementById("select-all");

  if (!selectAll) return;

  selectAll.addEventListener("change", () => {
    const visibleRows = document.querySelectorAll(
      'tbody tr:not([style*="display: none"])',
    );

    visibleRows.forEach((row) => {
      const checkbox = row.querySelector('input[name="selected"]');
      if (checkbox) checkbox.checked = selectAll.checked;
    });
    selectedItemsCount();
  });

  // Se houver uma nova pesquisa na barra reseta.
  const searchInput = document.getElementById("search-files");

  if (searchInput) {
    searchInput.addEventListener("input", () => {
      selectAll.checked = false;
    });
  }
}
document.addEventListener("DOMContentLoaded", selectAllCheckBox);

// Pesquisar
function enableSearch(inputId, targetSelector) {
  const searchInput = document.getElementById(inputId);

  if (!searchInput) return;

  searchInput.addEventListener("input", function () {
    const term = this.value.toLowerCase();
    const lines = document.querySelectorAll(targetSelector);

    lines.forEach((line) => {
      const text = line.textContent.toLowerCase();
      line.style.display = text.includes(term) ? "" : "none";
    });
  });
}
document.addEventListener("DOMContentLoaded", function () {
  enableSearch("search-files", "tbody tr");
});

// Contador de arquios para upload
function uploadFilesCount() {
  const countSpan = document.getElementById("upload_count");
  const filesInput = document.getElementById("upload_input");

  if (!filesInput || !countSpan) return;

  filesInput.addEventListener("change", function () {
    const totalFiles = filesInput.files.length;

    countSpan.textContent = `${totalFiles} arquivos selecionados.`;
  });
}
document.addEventListener("DOMContentLoaded", uploadFilesCount);

// Contador de arquivos selecionados
function selectedItemsCount() {
  const checkboxes = document.querySelectorAll(".checkbox");
  const selectedItems = [];

  if (!checkboxes.length) return;

  checkboxes.forEach((cb) => {
    if (cb.checked) {
      selectedItems.push(cb.value);
    }
  });

  const countSpan = document.getElementById("selected-items");
  countSpan.textContent = selectedItems.length;
}
document.addEventListener("DOMContentLoaded", () => {
  const checkboxes = document.querySelectorAll(".checkbox");
  if (!checkboxes.length) return;

  checkboxes.forEach((cb) => {
    cb.addEventListener("change", selectedItemsCount);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("toggle_password");
  const input = document.getElementById("id_password");
  const iconShow = document.getElementById("icon_show");
  const iconHide = document.getElementById("icon_hide");

  if (!toggle || !input) return;

  toggle.addEventListener("click", () => {
    input.type = input.type === "password" ? "text" : "password";

    if (iconShow.style.display === "block") {
      iconShow.style.display = "none";
      iconHide.style.display = "block";
    } else {
      iconShow.style.display = "block";
      iconHide.style.display = "none";
    }
  });
});
