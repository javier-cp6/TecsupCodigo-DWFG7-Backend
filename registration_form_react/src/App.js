// import './App.css';
import { useState } from 'react';

import './styles.css'
import event_img from './img/event_img.png'

function App() {
  const [ inputs, setInputs] = useState({}) 
  return (
    <main>
      <section class="section-container">
        <img class="img-home" src={event_img}/>
        <form class="form-container">
          <h2>Registro</h2>
          <input type="text" placeholder="Nombre*" value="" required/>
          <input type="text" placeholder="Apellido*" value="" required/>
          <input type="text" placeholder="Correo*" value="" required/>
          <input type="text" placeholder="Teléfono*" value="" required/>
          <input type="text" placeholder="Contraseña*" value="" required/>
          
          <h3>Zonas</h3>
          <p>Selecciona la zona de tu preferencia</p>
          <label><input type="radio" id="radio1" name="zone" value="1" checked/>Super VIP</label>
          <label><input type="radio" id="radio2" name="zone" value="2"/>VIP</label>
          <label><input type="radio" id="radio3" name="zone" value="3"/>General</label>
          <textarea></textarea>
          <label><input type="checkbox" id="cbox-tc" value="#"/>Acepto los términos y condiciones</label>
          <input type="submit" value="Registrarme"/>
        </form>
      </section>
    </main>
  );
}

export default App;
