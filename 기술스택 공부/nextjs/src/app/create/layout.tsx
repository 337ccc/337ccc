interface ILayoutProps {
  children: React.ReactNode;
};

export default function Layout(props: ILayoutProps) {
  return (
    <form>
      <h2>Create</h2>
      {props.children}
    </form>
  )
}