'use strict' 
const NodeHelper = require('node_helper'); 

const PythonShell = require('python-shell'); 
var pythonStarted = false; 

module.exports = NodeHelper.create({
	
	python_start: function () {
		const self = this; 
		const pyshell = new PythonShell('modules/' + this.name + '/SM_FaceRec.py', { mode: 'json', args: [JSON.stringify(this.config)]})
		
		pyshell.on('message', function(message){
			
			if(message.hasOwnProperty('status')){
				consule.log("[" + self.name + "] " + message.status); 
			}
			if(message.hasOwnProperty('login')){
				console.log("[" + self.name + "] " + "User: " + self.config.users[message.login.user - 1]);
				self.sendSocketNotification('user', {action: "login", user: message.login.user - 1}); 
			if(message.hasOwnProperty('logout')){
				console.log("[" + self.name + "] " + "User: " + self.config.users[message.logout.user - 1]);
				self.sendSocketNotification('user', {action: "login", user: message.logout.user - 1}); 
			}
			
		});
		
		pyshell.end(function (err) { 
			if (err) throw err; 
			console.log("finished running");
		});
		
	},
	
	socketNotificationReceived: function(notification, payload){
		if(notification === 'CONFIG'){
			this.config = payload
			if(!pythonStarted){
				pythonStarted = true; 
				this.python_start(); 
			};
		};
	}	
	
	
});
