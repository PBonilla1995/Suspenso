// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));
  var Datos=["","",""],validar=0, LED_D1=[], LED_D2=[],Doc=[]; 
  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
    useSSL: false,
    userName: "patriciabonilla1995@gmail.com",
    password: "1726646654",
    onSuccess:onConnect,
    onFailure:doFail
    
  }
  
  // connect the client
  client.connect(options);
    
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
    client.subscribe("patriciabonilla1995@gmail.com/test");
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    
    console.log(message.payloadString);
    Datos=(message.payloadString).split(("-"));
    if(Datos[0]=="Led"){
      Data=[Datos[1],Datos[2]];
      MisDAtos(Data);
    }
    if(Datos[0]=="Datos"){
      var tres=document.getElementById("Historial");
      var cautro=document.getElementById("Historial1");
      tres.innerHTML=Datos[1];
      cautro.innerHTML=Datos[2];
      
    }
    
  }

  function MisDAtos(texto){
    var uno=document.getElementById("LED_1");
    var dos=document.getElementById("LED_2");
    
    uno.innerHTML=" Se encuentra "+texto[0];
    dos.innerHTML="Se encuentra "+texto[1];
  }
  

  function MostarDatos(){
    mensaje("0");
  }
  
  
  function mensaje(text){
    message = new Paho.MQTT.Message(text);
    message.destinationName = "patriciabonilla1995@gmail.com/test1";
    client.send(message);
  }


 