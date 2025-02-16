
// let lists = document.getElementById("list-group")

// GET, access_task_list
const getTaskList = async (username) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/${username}`, {
    method: "GET",
    });

    if (!response.ok) {
      throw new Error("Failed to access task list.");
    }
    return await response.json(); // assuming it returns a JSON array of tasks

  } catch (error) {
    console.error("Error accessing task list:", error);
    return [];
  }
};

const renderTaskList = async (username: string) => {
  const tasks = await(getTaskList(username))

  const fullList = document.getElementById("list-group");
  if (fullList) {
    fullList.innerHTML = ""; // clearing previous tasks
  }

  tasks.forEach((task: { name: string; done: boolean; repeat: boolean; }) => {
    const taskItem = document.createElement("li")
    taskItem.className = "task-item";

    taskItem.innerHTML = `
      <span class="task-name">${task.name}</span>
      <button class="check-box">${task.done ? "✔️" : "x"}</button>
      <button class="up-arrow">↑</button>
      <button class="down-arrow">↓</button>
      <button class="delete-button">🗑️</button>
    `;

    fullList?.appendChild(taskItem)
    addEventListenersToTask(taskItem, task.name, username); // this helper method for event listeners
  });

}

// new_task, POST
const createTask = async (username, taskName, doesRepeat) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
              task_name: taskName,
              reoccur: doesRepeat
          })

        });
    
        if (!response.ok) {
          throw new Error("Failed to add task.");
        }

        await renderTaskList(username)

      } catch (error) {
        console.error("Error adding task:", error);
      }
};

// create_task API path

let form = document.getElementById("task-form")
form?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = (document.getElementById("username") as HTMLInputElement).value.trim();
    const taskName = (document.getElementById("task-name") as HTMLInputElement).value.trim();
    const doesRepeat = (document.getElementById("task-recur") as HTMLInputElement).checked;

    (document.getElementById("task-name") as HTMLInputElement).value = "";
    (document.getElementById("task-recur") as HTMLInputElement).checked = false;

    await createTask(username, taskName, doesRepeat);
});

// PATCH, reset_list
const reset_list = async(username) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/${username}`, {
      method: "PATCH",
    });

    if (!response.ok) {
      throw new Error("Failed to reset task list.");
    }

    await renderTaskList(username); 

  } catch (error) {
    console.error("Error resetting task list:", error);
  }
};

let resetButton = document.getElementById("reset")
resetButton?.addEventListener("click", async (event) => {
  const username = (document.getElementById("username") as HTMLInputElement).value.trim();
  if (!username) {
      alert("Please enter a username to reset the task list.");
      return;
  }
  await reset_list(username);
});


// toggle_check, PATCH
const toggleCheck = async (username, taskName) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}`, {
          method: "PATCH",
        });

        if (!response.ok) {
          throw new Error("Failed to change task completion.");
          
        }

        await renderTaskList(username)

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
  
      await renderTaskList(username)

      if (!response.ok) {
        throw new Error("Failed to delete task.");
      }
    } catch (error) {
      console.error("Error deleting task:", error);
    }
  };

// shift_position, PATCH
const moveUp = async (username, taskName) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}/up`, {
        method: "PATCH",
      });
  
      await renderTaskList(username)

      if (!response.ok) {
        throw new Error("Failed to adjust task priority.");
      }
    } catch (error) {
      console.error("Error adjusting task priority:", error);
    }
  };

  // shift_position, PATCH --> UP
const moveDown = async (username, taskName) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/${username}/${taskName}/down`, {
      method: "PATCH",
    });

    await renderTaskList(username)

    if (!response.ok) {
      throw new Error("Failed to adjust task priority.");
    }
  } catch (error) {
    console.error("Error adjusting task priority:", error);
  }
};


// this is a helper method to update each task with event handlers
const addEventListenersToTask = (task: HTMLElement, taskName: string, username: string) => {
  const deleteButton = task.querySelector(".delete-button") as HTMLButtonElement;
  deleteButton?.addEventListener("click", (e: MouseEvent) => {
    e.stopPropagation();
    deleteTask(username, taskName);
  });

  const checkBox = task.querySelector(".check-box") as HTMLButtonElement;
  checkBox?.addEventListener("click", (e: MouseEvent) => {
    e.stopPropagation();
    toggleCheck(username, taskName).then(() => renderTaskList(username));
  });

  const upArrow = task.querySelector(".up-arrow") as HTMLButtonElement;
  upArrow?.addEventListener("click", (e: MouseEvent) => {
    e.stopPropagation();
    moveUp(username, taskName).then(() => renderTaskList(username));
  });

  const downArrow = task.querySelector(".down-arrow") as HTMLButtonElement;
  downArrow?.addEventListener("click", (e: MouseEvent) => {
    e.stopPropagation();
    moveDown(username, taskName).then(() => renderTaskList(username));
  });
};