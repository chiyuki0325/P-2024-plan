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
          style={{
            gridRow: Math.ceil(index / 3), 
            gridColumn: (index % 3 || 3 )
        }}
          onButtonClick={appendExpression}
        />
      ))}
      <CalcButton key="back" char="🔙" onButtonClick={backspace} style={{
          gridRow: 3,
          gridColumn: 2
      }}/>
    </div>
  )
}
