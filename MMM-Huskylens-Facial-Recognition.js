/* global Module */


Module.register('MMM-Huskylens-Facial-Recognition', {
	
	defaults: {
		//Recognition interval in seconds
		interval: 2, 
		// Logout delay after last recognition so that a user does not get instantly logged out if they turn away from the mirror for a few seconds
		logoutDelay: 15,
		// Array with usernames
		users: [],
		//Module set used for strangers & if no user is detected
		defaultClass: "default", 
		//Set of modules which are shown for every user
		everyoneClass: "everyone", 
		//Boolean to toggle welcomeMessage
		welcomeMessage: true,
	},
	
	// Define required translations.
	getTranslations: function() {
		return{
			en: "translations/en.json"
		};
	},
	
	login_user: function() {
		var self = this; 
		
		MM.getModules().withClass(this.config.defaultClass).exceptWithClass(this.config.everyoneClass).enumerate(function(module){
			module.hide(1000, function() {
				Log.log(module.name + ' is hidden.'); 
			}, {lockString: self.identifier});
		});
		
		MM.getModules().withClass(this.current_user).enumerate(function(module) {
			module.show(1000, function() {
				Log.log(module.name + 'is shown.'); 
			}, {lockString: self-identifier}); 
		}); 
		
		this.sendNotification("CURRENT_USER", "None");
	},
	
	// Override socket notification handler.
	socketNotificationReceived: function(notification, payload) {
		if(payload.action == "login"){
			if(this.current_user_id != payload.user){
				this.logout_user()
			}
			if(payload.user == -1){
				this.current_user = this.translate("stranger")
				this.current_user_id = payload.user;
			}
			else{
				this.current_user = this.config.users[payload.user];
				this.current_user_id = payload.user;
				this.login_user()
			}
			
			if(this.config.welcomeMessage){
				this.sendNotification("SHOW_ALERT", {type: "notification", message: this.translate("message").replace("%person", this.current_user), title: this.translate("title")});
			}
		}
		else if (payload.action == "logout"){
			this.logout_user()
			this.current_user = null;
		}
	},
	
	notificationReceived: function(notification, payload, sender) {
		if(notification === 'DOM_OBJECTS_CREATED') {
			var self = this;
			
			MM.getModules().exceptWithClass("default").enumerate(function(module){
				module.hide(1000, function() {
					Log.log('Module is hidden.');
				}, {lockString: self.identifier});
			});
		}
	},
	
	start: function(){
		this.current_user = null;
		this.sendSocketNotification('CONFIG', this.config);
		Log.info('Starting module: ' + this.name); 
	}
				
