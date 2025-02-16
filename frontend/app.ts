
let lists = document.getElementById("list-group")

// new_task, POST
const createTask = async (username, taskName) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}`, {
          method: "POST",
        });
    
        if (!response.ok) {
          throw new Error("Failed to add task.");
        }
      } catch (error) {
        console.error("Error adding task:", error);
      }
};


// toggle_check, PATCH
const toggleCheck = async (username, taskName) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}`, {
          method: "PATCH",
        });
    
        if (!response.ok) {
          throw new Error("Failed to change task completion.");
        }
      } catch (error) {
        console.error("Error changing task completion:", error);
      }
};

// delete_task, DELETE
const deleteTask = async (username, taskName) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}`, {
        method: "DELETE",
      });
  
      if (!response.ok) {
        throw new Error("Failed to delete task.");
      }
    } catch (error) {
      console.error("Error deleting task:", error);
    }
  };



let form = document.getElementById("task-form")
form?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const taskName = (document.getElementById("task-name") as HTMLInputElement).value;
    const doesRepeat = (document.getElementById("task-recur") as HTMLInputElement).checked;
    // TODO const username = ____

    (document.getElementById("task-name") as HTMLInputElement).value = "";
    (document.getElementById("task-recur") as HTMLInputElement).checked = false;

    await createTask(taskName, doesRepeat);
});