import { Title1 } from "@fluentui/react-components"

export default function CalcTitle() {
  return (
    <>
      <Title1
        style={{
          display: "flex",
          flexDirection: "row",
          gap: "8px",
        }}
      >
        <img src="pioneer-chicken.png" />
        先锋🐔算器
      </Title1>
    </>
  )
}
