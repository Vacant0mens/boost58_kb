// Arduino ProMicro atmega32u4au
// Params
//  orientation: default is down
//    if down, power led will face the pcb
//    if up, power led will face away from pcb

module.exports = {
    params: {
      designator: 'MCU',
      reversible: false,
      via_size: 0.8,
      via_drill: 0.4,
      LED: {type: 'net', value: 'LED'},
      RAW: {type: 'net', value: 'RAW'},
      GND: {type: 'net', value: 'GND'},
      RST: {type: 'net', value: 'RST'},
      VCC: {type: 'net', value: 'VCC'},
      D29: {type: 'net', value: 'D29'},
      D28: {type: 'net', value: 'D28'},
      D27: {type: 'net', value: 'D27'},
      D26: {type: 'net', value: 'D26'},
      D22: {type: 'net', value: 'D22'},
      D20: {type: 'net', value: 'D20'},
      D23: {type: 'net', value: 'D23'},
      D21: {type: 'net', value: 'D21'},
      D1: {type: 'net', value: 'D1'},
      D0: {type: 'net', value: 'D0'},
      D2: {type: 'net', value: 'D2'},
      D3: {type: 'net', value: 'D3'},
      D4: {type: 'net', value: 'D4'},
      D5: {type: 'net', value: 'D5'},
      D6: {type: 'net', value: 'D6'},
      D7: {type: 'net', value: 'D7'},
      D8: {type: 'net', value: 'D8'},
      D9: {type: 'net', value: 'D9'}
    },
    body: p => {
      const standard = `
        (module SparkFunProMicroQwiic (layer F.Cu) (tedit 5B307E4C)
        ${p.at /* parametric position */}
  
        ${'' /* footprint reference */}
        (fp_text reference "${p.ref}" (at 0 0) (layer F.SilkS) ${p.ref_hide} (effects (font (size 1.27 1.27) (thickness 0.15))))
        (fp_text value "" (at 0 0) (layer F.SilkS) hide (effects (font (size 1.27 1.27) (thickness 0.15))))
      
        ${''/* illustration of the (possible) USB port overhang */}
        (fp_line (start -19.304 -3.81) (end -14.224 -3.81) (layer Dwgs.User) (width 0.15))
        (fp_line (start -19.304 3.81) (end -19.304 -3.81) (layer Dwgs.User) (width 0.15))
        (fp_line (start -14.224 3.81) (end -19.304 3.81) (layer Dwgs.User) (width 0.15))
        (fp_line (start -14.224 -3.81) (end -14.224 3.81) (layer Dwgs.User) (width 0.15))
      
        ${''/* component outline */}
        (fp_line (start -17.78 8.89) (end 15.24 8.89) (layer F.SilkS) (width 0.15))
        (fp_line (start 15.24 8.89) (end 15.24 -8.89) (layer F.SilkS) (width 0.15))
        (fp_line (start 15.24 -8.89) (end -17.78 -8.89) (layer F.SilkS) (width 0.15))
        (fp_line (start -17.78 -8.89) (end -17.78 8.89) (layer F.SilkS) (width 0.15))
        `
      function pin_names(def_neg, def_pos) {
        return `
          ${''/* extra border around "RAW", in case the rectangular shape is not distinctive enough */}
          (fp_line (start -15.24 ${def_pos}6.35) (end -12.7 ${def_pos}6.35) (layer F.SilkS) (width 0.15))
          (fp_line (start -15.24 ${def_pos}6.35) (end -15.24 ${def_pos}8.89) (layer F.SilkS) (width 0.15))
          (fp_line (start -12.7 ${def_pos}6.35) (end -12.7 ${def_pos}8.89) (layer F.SilkS) (width 0.15))
        
          ${''/* pin names */}
          (fp_text user LED (at -16.41 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user RAW (at -13.97 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user GND (at -11.43 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user RST (at -8.89 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user VCC (at -6.35 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D29 (at -3.81 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D28 (at -1.27 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D27 (at 1.27 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D26 (at 3.81 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D22 (at 6.35 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D20 (at 8.89 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D23 (at 11.43 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D21 (at 13.97 ${def_pos}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
        
          (fp_text user D1 (at -13.97 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D0 (at -11.43 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user GND (at -8.89 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user GND (at -6.35 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D2 (at -3.81 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D3 (at -1.27 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D4 (at 1.27 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D5 (at 3.81 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D6 (at 6.35 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D7 (at 8.89 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D8 (at 11.43 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          (fp_text user D9 (at 13.97 ${def_neg}4.8 ${p.r + 90}) (layer F.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15))))
          `
      }
      function pins(def_neg, def_pos, side) {
        return `
            ${''/* the actual pins */}
          (pad "LED" smd circle (at -16.41 ${def_pos}7.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.LED})
          (pad "RAW" smd rect (at -13.97 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.RAW})
          (pad "GND" smd rect (at -11.43 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.GND})
          (pad "RST" smd rect (at -8.89 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.RST})
          (pad "VCC" smd rect (at -6.35 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.VCC})
          (pad "29" smd rect (at -3.81 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D29})
          (pad "28" smd rect (at -1.27 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D28})
          (pad "27" smd rect (at 1.27 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D27})
          (pad "26" smd rect (at 3.81 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D26})
          (pad "22" smd rect (at 6.35 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D22})
          (pad "20" smd rect (at 8.89 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D20})
          (pad "23" smd rect (at 11.43 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D23})
          (pad "21" smd rect (at 13.97 ${def_pos}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D21})
          
          (pad "1" smd rect (at -13.97 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D1})
          (pad "0" smd rect (at -11.43 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D0})
          (pad "GND" smd rect (at -8.89 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.GND})
          (pad "GND" smd rect (at -6.35 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.GND})
          (pad "2" smd rect (at -3.81 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D2})
          (pad "3" smd rect (at -1.27 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D3})
          (pad "4" smd rect (at 1.27 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D4})
          (pad "5" smd rect (at 3.81 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D5})
          (pad "6" smd rect (at 6.35 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D6})
          (pad "7" smd rect (at 8.89 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D7})
          (pad "8" smd rect (at 11.43 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D8})
          (pad "9" smd rect (at 13.97 ${def_neg}8.62 ${p.r}) (size 1.7526 1.7526) (layers "${side}.Cu" "${side}.Paste" "${side}.Mask") ${p.D9})
        `
      }
      function pin_names_reversed (def_neg, def_pos) {
        return `      
        ${''/* component outline */}
        (fp_line (start -17.78 8.89) (end 15.24 8.89) (layer B.SilkS) (width 0.15))
        (fp_line (start 15.24 8.89) (end 15.24 -8.89) (layer B.SilkS) (width 0.15))
        (fp_line (start 15.24 -8.89) (end -17.78 -8.89) (layer B.SilkS) (width 0.15))
        (fp_line (start -17.78 -8.89) (end -17.78 8.89) (layer B.SilkS) (width 0.15))

        ${''/* pin names */}
        (fp_text user LED (at -16.41 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user RAW (at -13.97 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user GND (at -11.43 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user RST (at -8.89 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user VCC (at -6.35 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D29 (at -3.81 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D28 (at -1.27 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D27 (at 1.27 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D26 (at 3.81 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D22 (at 6.35 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D20 (at 8.89 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D23 (at 11.43 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D21 (at 13.97 ${def_pos}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
      
        (fp_text user D1 (at -13.97 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D0 (at -11.43 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user GND (at -8.89 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user GND (at -6.35 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D2 (at -3.81 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D3 (at -1.27 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D4 (at 1.27 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D5 (at 3.81 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D6 (at 6.35 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D7 (at 8.89 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D8 (at 11.43 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        (fp_text user D9 (at 13.97 ${def_neg}4.8 ${p.r + 90}) (layer B.SilkS) (effects (font (size 0.8 0.8) (thickness 0.15)) (justify mirror)))
        `
      }
      function reversible_vias () {
        return `
        (via (at ${p.eaxy(-17, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.LED.index}))
        (via (at ${p.eaxy(-15.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.RAW.index}))
        (via (at ${p.eaxy(-14, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D1.index}))
        (via (at ${p.eaxy(-12.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D0.index}))
        (via (at ${p.eaxy(-11, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.RST.index}))
        (via (at ${p.eaxy(-9.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.GND.index}))
        (via (at ${p.eaxy(-8, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.VCC.index}))
        (via (at ${p.eaxy(-6.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D2.index}))
        (via (at ${p.eaxy(-5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D29.index}))
        (via (at ${p.eaxy(-3.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D3.index}))
        (via (at ${p.eaxy(-2, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D28.index}))
        (via (at ${p.eaxy(-0.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D4.index}))
        (via (at ${p.eaxy(1, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D27.index}))
        (via (at ${p.eaxy(2.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D5.index}))
        (via (at ${p.eaxy(4, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D26.index}))
        (via (at ${p.eaxy(5.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D6.index}))
        (via (at ${p.eaxy(7, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D22.index}))
        (via (at ${p.eaxy(8.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D7.index}))
        (via (at ${p.eaxy(10, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D20.index}))
        (via (at ${p.eaxy(11.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D8.index}))
        (via (at ${p.eaxy(13, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D23.index}))
        (via (at ${p.eaxy(14.5, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D9.index}))
        (via (at ${p.eaxy(16, 0)}) (size ${p.via_size}) (drill ${p.via_drill}) (layers "F.Cu" "B.Cu") (net ${p.D21.index}))
        `
      }
      let final = `
        ${standard}
        ${pins('', '-', 'F')}
        ${p.reversible ? pins('-', '', 'B') : ''}
        ${pin_names('', '-')}
        ${p.reversible ? pin_names_reversed('-', '') : ''}
        )
      `
        // ${p.reversible ? reversible_vias() : ''}
      return final
    }
  }