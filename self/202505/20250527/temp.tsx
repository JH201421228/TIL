import "@/customCss/ImageEdit/InpaintBrushSection.css";
import { useEffect, useState } from "react";
import type { KeyboardEvent } from "react";
import ColorPicker from "@/components/Common/ColorPicker";
import SizeSlider from "@/components/Common/SizeSlider";

const InpaintBrushSection = () => {
  const [color, setColor] = useState("#000000");
  const [transparency, setTransparency] = useState(1);
  const [size, setSize] = useState(1);
  const [displayColorPicker, setDisplayColorPicker] = useState(false);
  const [tempTransparency, setTempTransparency] = useState("100");

  useEffect(() => {
    setTempTransparency(String(Math.floor(transparency * 100)));
  }, [transparency]);

  const handleClick = () => {
    setDisplayColorPicker(!displayColorPicker);
  };

  const handleTransparencyKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      const value = Number(tempTransparency);
      if (value >= 0 && value <= 100) {
        setTransparency(value / 100);
      } else {
        setTempTransparency(String(Math.floor(transparency * 100)));
      }
    }
  };

  const handleTransparencyBlur = () => {
    const value = Number(tempTransparency);
    if (value >= 0 && value <= 100) {
      setTransparency(value / 100);
    } else {
      setTempTransparency(String(Math.floor(transparency * 100)));
    }
  };

  return (
    <div className="inpaint-brush-section">
      <div className="inpaint-brush-section-upper-box">
        <svg
          width="16px"
          height="16px"
          viewBox="0 0 16 16"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M9.44444 4.44444L12.3917 0.760432C12.7762 0.279794 13.3583 0 13.9738 0C15.0929 0 16 0.907148 16 2.02617C16 2.64169 15.7202 3.22383 15.2396 3.60835L11.5556 6.55556L12.2454 7.24538C12.7286 7.72855 13 8.38388 13 9.0672C13 9.66992 12.7887 10.2536 12.4028 10.7166L11.8246 11.4104L4.58957 4.17536L5.2834 3.59717C5.74643 3.21131 6.33008 3 6.9328 3C7.61612 3 8.27145 3.27145 8.75462 3.75462L9.44444 4.44444Z"
            fill="currentColor"
          />
          <path
            d="M0 8L3.04679 5.46101L10.539 12.9532L8 16L0 8Z"
            fill="currentColor"
          />
        </svg>
        Inpaint Brush
      </div>
      <div className="inpaint-brush-section-middle-box" onClick={handleClick}>
        <div className="inpaint-brush-section-middle-box-left">
          <div
            className="inpaint-brush-section-middle-box-left-color-box"
            style={{ backgroundColor: color }}
          />
          {color}
        </div>
        <div className="inpaint-brush-section-middle-box-right">
          <input
            type="number"
            className="inpaint-brush-transparency-input"
            value={tempTransparency}
            onChange={(e) => setTempTransparency(e.target.value)}
            onKeyDown={handleTransparencyKeyDown}
            onBlur={handleTransparencyBlur}
            min={0}
            max={100}
          />
          %
        </div>
      </div>
      <SizeSlider size={size} setSize={setSize} />
      <ColorPicker
        setColor={setColor}
        color={color}
        setDisplayColorPicker={setDisplayColorPicker}
        displayColorPicker={displayColorPicker}
        setTransparency={setTransparency}
        transparency={transparency}
      />
    </div>
  );
};

export default InpaintBrushSection;