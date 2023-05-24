#!/usr/bin/node
const request = require('request');

function completedTasks (apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error occurred while making GET request:');
      console.error(error);
    } else {
      const todos = JSON.parse(body);
      const completedTasks = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId;
          if (completedTasks[userId]) {
            completedTasks[userId]++;
          } else {
            completedTasks[userId] = 1;
          }
        }
      });
      console.log(completedTasks);
    }
  });
}

const apiUrl = process.argv[2];
completedTasks(apiUrl);
