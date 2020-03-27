<script>
  function checkLoginState() {
    FB.login(function (response) {
        //print accessToken
        console.log(response);
        //set what user's FB information would be got
        var fields = ['id','gender','age_range', 'email', 'first_name', 'last_name', 'link', 'name','updated_time'];
        var graphApiUrl = 'https://graph.facebook.com/v2.5/me?fields=' + fields.join(',');
                    if (response.authResponse) {
                        FB.api(graphApiUrl, function (response) {
                            //print user's FB information
                            console.log(response);
                        });
                        FB.api('/me/friends', function(response) {
                          //print user's friend data ( only user's friend who has been used this app and accessed protocal )
                          console.log(response);
                        });
                        FB.api('/me', function(response) {     
                          //print user's picture ( large type ) 
                            document.getElementById('login').innerHTML = '<img src="http://graph.facebook.com/' + response.id + '/picture?type=large" />';
                        });
                    }
                    else {
                        alert("User did not login successfully");
                    }
                }, { scope: 'email,user_friends' });
  }
  //fb logout function
  function logout(){
    FB.logout(function(response) {
      // user is now logged out
    });
  }
  window.fbAsyncInit = function() {
      FB.init({
        appId      : '234522136889531',
        cookie     : true,  // enable cookies to allow the server to access 
                            // the session
        xfbml      : true,  // parse social plugins on this page
        version    : 'v2.5' // use graph api version 2.5
      });

  };
  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
</script>

//HTML code
//fb login and logout button 
/*<fb:login-button scope="email" onlogin="checkLoginState()">
        </fb:login-button>
        <button onclick="logout()">logout</button>
        <div id="login">
        </div>
*/