export function tabla(parametro1,parametro2){
  //Tomo el div con el id container para insertar html dentro de este (linea 25)
    const container = document.getElementById('container')

  // CALCULOS TABLA CENTRIFUGA
    const rp = Math.floor(parametro1 * 0.3190995427365)
    const gas = Math.floor((parametro1 * 511.13199046407) / 1000)
    const gCapex = Math.floor((parametro1 * 0.0035174111853) * (1925000 / 0.88))
    const gOpex = Math.floor(gCapex * 0.03)
  
    const solarCapex = Math.floor(parametro1 * 0.0035174111853)
    const ft = Math.floor(solarCapex * 1000000)
    const eCapex = Math.floor(solarCapex * 1700000)
    const bCapex = Math.floor(solarCapex * 2000000)
  
    // CALCULOS TABLA ABSORCION
    const gasAbsorcion = Math.floor((parametro2 * 511.13199046407) / 1000)
    const gasCapexAbsorcion = Math.floor(((parametro2 * 0.0035174111853) * (1925000 / 0.88)))
    const gasOpexAbsorcion = Math.floor(gasCapexAbsorcion * 0.03)
  
    const solarCapexAbsorcion = Math.floor(parametro2 * 0.0035174111853)
    // const ftAbsorcion = (solarCapexAbsorcion * 1000000) * 1.015
    const bioAbsorcion = Math.floor(solarCapexAbsorcion * 2000000)
    
    // ejecuto el container y le paso un html con comillas ` `
    container.innerHTML= `

        <h1 class="table-title">Centrifugo</h1>

        <table class="table-content">
          <thead>
            <tr>
              <th><h3>Energia</h3></th>
              <th><h3>Emisiones</h3></th>
              <th><h3>Capex</h3></th>
              <th><h3>Opex</h3></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Red Publica</td>
              <td>${rp}</td>
              <td>${0}</td>
              <td>${0}</td>
            </tr>
            <tr>
              <td>Microturbina Gas</td>
              <td>${gas}</td>
              <td>${gCapex}</td>
              <td>${gOpex}</td>
            </tr>
            <tr>
              <td>Solar Fotovoltaica</td>
              <td>${ft}</td>
              <td>${solarCapex}</td>
              <td>${0}</td>
            </tr>
            <tr>
              <td>Energia Eolica</td>
              <td>${0}</td>
              <td>${eCapex}</td>
              <td>${0}</td>
            </tr>
            <tr>
              <td>Energia Biomasa</td>
              <td>${0}</td>
              <td>${bCapex}</td>
              <td>${0}</td>
            </tr>
            <tr>
              <td>Toneladas de refrigeracion que sumistran <br /> los chillers
                de adsorcion seleccionados es:
              </td>
              <td>${parametro1}</td>
              <td>${0}</td>
              <td>${0}</td>
            </tr>
          </tbody>
        </table>

        <h1 class="table-title">Absorción</h1>
        <table class="table-content">
          <thead>
            <tr>
              <th><h3>Energia</h3></th>
              <th><h3>Emisiones</h3></th>
              <th><h3>Capex</h3></th>
              <th><h3>Opex</h3></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Microturbina Gas</td>
              <td>${gasAbsorcion}</td>
              <td>${gasCapexAbsorcion}</td>
              <td>${gasOpexAbsorcion}</td>
            </tr>
            <tr>
              <td>Solar Termica</td>
              <td>${0}</td>
              <td>${solarCapexAbsorcion}</td>
              <td>${0}</td>
            </tr>
            <tr>
              <td>Energia Biomasa</td>
              <td>${0}</td>
              <td>${bioAbsorcion}</td>
              <td>${0}</td>
            </tr>
            <tr>
              <td>Toneladas de refrigeracion que sumistran <br /> los chillers
                de adsorcion seleccionados es:
              </td>
              <td>${parametro2}</td>
              <td>${0}</td>
              <td>${0}</td>
            </tr>
          </tbody>
        </table>
    
    `
}