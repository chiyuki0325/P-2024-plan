import CalcButton from "./CalcButton.jsx"

export default function CalcButtonMatrix({ appendExpression }) {
  return (
    <div className="buttons-grid">
      {["1", "2", "3", "4", "5", "6", "7", "8", "9"].map((char) => (
        <CalcButton
          key={char}
          char={char}
          style={{
            gridRow: Math.ceil(char / 3),
            gridColumn: (char % 3) || 3,
          }}
          onButtonClick={appendExpression}
        />
      ))}

      <CalcButton
        char="0"
        style={{
          gridRow: 4,
          gridColumn: 1,
        }}
        onButtonClick={appendExpression}
      />
      
      <CalcButton
        char="."
        style={{
          gridRow: 4,
          gridColumn: 2,
        }}
        onButtonClick={appendExpression}
      />
    </div>
  )
}
