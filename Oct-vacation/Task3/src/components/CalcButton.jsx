import { Button } from "@fluentui/react-components"

export default function CalcButton({ char, onButtonClick, r, c }) {
  return (
    <Button
      className="calc-button"
      onClick={() => onButtonClick(char)}
      style={{
        gridRow: r,
        gridColumn: c,
      }}
    >
      {char}
    </Button>
  )
}
