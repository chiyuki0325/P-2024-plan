import { Title2 } from "@fluentui/react-components"

export default function CalcResult({ result }) {
  return (
    <div className="calc-result">
      <span>计算结果是:</span>
      <Title2 style={{
        position: "relative",
        top: "-6px",
      }}>{result}</Title2>
    </div>
  )
}
