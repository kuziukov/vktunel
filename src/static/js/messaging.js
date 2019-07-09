// Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyBlhrjca3zMlH1KPpSj2o3YbxZHj13ik7o",
    authDomain: "wlusmru.firebaseapp.com",
    databaseURL: "https://wlusmru.firebaseio.com",
    projectId: "wlusmru",
    storageBucket: "",
    messagingSenderId: "900983135054",
    appId: "1:900983135054:web:7728e4e4579aa38b"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  function sendSubscriptionToBackEnd(subscription) {
      $.post(
          "{{ url_for('api.fcmsubscriptionpost') }}",
          JSON.stringify(subscription)
      );
    }

  function urlBase64ToUint8Array(base64String) {
      const padding = '='.repeat((4 - base64String.length % 4) % 4);
      const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/')
      ;
      const rawData = window.atob(base64);
      return Uint8Array.from([...rawData].map((char) => char.charCodeAt(0)));
    }

    function subscribeUserToPush(key) {
      return navigator.serviceWorker.register('static/js/sw.js')
      .then(function(registration) {
        const subscribeOptions = {
          userVisibleOnly: true,
          applicationServerKey: urlBase64ToUint8Array(
            'BE_nppho7w0rkGST4UV1o_ISr4ljQtUYMbf9NkGB2cFcwudSarSskpH7-NEhSbUEvwj004n3IZi130Xfu3GXNzE'
          )
        };

        return registration.pushManager.subscribe(subscribeOptions);
      })
      .then(function(pushSubscription) {
        console.log('Received PushSubscription: ', JSON.stringify(pushSubscription));
        sendSubscriptionToBackEnd(pushSubscription);
        return pushSubscription;
      });
    }

  function requestPermission() {
      return new Promise(function(resolve, reject) {
        const permissionResult = Notification.requestPermission(function(result) {
          // Поддержка устаревшей версии с функцией обратного вызова.
          resolve(result);
        });
        if (permissionResult) {
          permissionResult.then(resolve, reject);
        }
      })
      .then(function(permissionResult) {
        if (permissionResult !== 'granted') {
          throw new Error('Permission not granted.');
        }
        subscribeUserToPush('key')
      });
      return true;
    }


  if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('static/js/sw.js')
        .then(function() {
          console.log('SW registered');
          requestPermission()
        });
    }
