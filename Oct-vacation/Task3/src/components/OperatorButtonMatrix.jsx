import CalcButton from "./CalcButton.jsx"

export default function OperatorButtonMatrix({ appendExpression, backspace }) {
  return (
    <div className="buttons-grid operators">
      {[
        ["+", 1],
        ["-", 2],
        ["(", 3],
        ["*", 4],
        ["/", 5],
        [")", 6],
        ["^", 7],
      ].map(([char, index]) => (
        <CalcButton
          key={char}
          char={char}
          r={Math.ceil(index / 3)}
          c={index % 3 || 3}
          onButtonClick={appendExpression}
        />
      ))}
      <CalcButton key="back" char="🔙" onButtonClick={backspace} r={3} c={3} />
    </div>
  )
}
