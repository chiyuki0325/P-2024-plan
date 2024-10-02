import CalcButton from "./CalcButton.jsx"

export default function CalcButtonMatrix({ appendExpression }) {
  return (
    <div className="buttons-grid">
      {["1", "2", "3", "4", "5", "6", "7", "8", "9"].map((char) => (
        <CalcButton
          key={char}
          char={char}
          r={Math.ceil(char / 3)}
          c={(char % 3) || 3}
          onButtonClick={appendExpression}
        />
      ))}

      <CalcButton
        char="0" r={4} c={1}
        onButtonClick={appendExpression}
      />
      
      <CalcButton
        char="." r={4} c={2}
        onButtonClick={appendExpression}
      />
    </div>
  )
}
