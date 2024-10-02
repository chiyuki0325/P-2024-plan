import { useState } from "react"
import "./App.css"
import calculate from "./js/calculator.js"

import { Card } from "@fluentui/react-components"

import CalcTextField from "./components/CalcTextField.jsx"
import CalcTitle from "./components/CalcTitle.jsx"
import CalcResult from "./components/CalcResult.jsx"
import CalcButtonMatrix from "./components/CalcButtonMatrix.jsx"
import OperatorButtonMatrix from "./components/OperatorButtonMatrix.jsx"

function App() {
  const [value, setValue] = useState("")
  const [result, setResult] = useState(0)
  const [validationState, setValidationState] = useState("none")

  function setExpression(expr) {
    // 更改表达式并触发计算
    setValue(expr)

    if (expr === '') {
      setResult(0)
      return setValidationState("none")
    }

    try {
      setResult(calculate(expr))
      return setValidationState("none")
    } catch (e) {
      setValidationState("error")
    }
  }

  function onExpressionChanged(event, data) {
    // Textarea 内容变化时更新表达式
    return setExpression(data.value)
  }

  function appendExpression(char) {
    // 点击 UI 按钮时更新表达式
    return setExpression(value + char)
  }

  function backspace(_) {
    return setExpression(value.slice(0, -1))
  }

  return (
    <>
      <Card className="calculator-root">
        <CalcTitle />
        <CalcTextField
          {...{
            value,
            onChange: onExpressionChanged,
            validationState,
          }}
        />
        <CalcButtonMatrix {...{
          appendExpression
        }}/>

        <OperatorButtonMatrix {...{
          appendExpression, backspace
        }}  />
        <CalcResult result={result} />
      </Card>
    </>
  )
}

export default App
