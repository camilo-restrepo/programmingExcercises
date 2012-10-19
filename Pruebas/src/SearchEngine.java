import java.io.File;
import java.io.IOException;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.queryParser.ParseException;
import org.apache.lucene.queryParser.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopScoreDocCollector;
import org.apache.lucene.store.LockObtainFailedException;
import org.apache.lucene.store.MMapDirectory;
import org.apache.lucene.util.Version;


public class SearchEngine {

	/**
	 * Campos para indexamiento
	 */
	public final static String ESPECIE = "especie";
	public final static String NOMBRE = "nombre";
	public final static String CONTENT = "content";
	public final static String INDEX_PATH = "C:\\Users\\Pisco\\Downloads\\indexDir\\";
	public final static String INDEX_FILE = INDEX_PATH+"index";

	/**
	 * Directorio del indice
	 */
	private MMapDirectory idx;
	/**
	 * Analizador de Lucene
	 */
	private StandardAnalyzer analyzer;
	/**
	 * Instancia de la clase
	 */
	private static SearchEngine instancia;

	/**
	 * Devuelve la instancia de la clase
	 * @return instancia La instancia de la clase
	 * @throws CorruptIndexException
	 * @throws LockObtainFailedException
	 * @throws IOException 
	 */
	public static SearchEngine darInstancia() throws CorruptIndexException, LockObtainFailedException, IOException{
		if(instancia==null)
			instancia = new SearchEngine();
		return instancia;
	}

	/**
	 * Constructor privado para implementar el patron singleton
	 * @throws CorruptIndexException
	 * @throws LockObtainFailedException
	 * @throws IOException 
	 */
	private SearchEngine() throws CorruptIndexException, LockObtainFailedException, IOException {
		idx = new MMapDirectory(new File(INDEX_FILE));
		analyzer = new StandardAnalyzer(Version.LUCENE_36);
	}

	/**
	 * Permite resolver una busqueda
	 * @param query La busqueda ingresada por el usuario
	 * @return Lista con los resultados de la busqueda
	 * @throws ParseException
	 * @throws CorruptIndexException
	 * @throws IOException 
	 */
	public void search(String query) throws ParseException, CorruptIndexException, IOException {
		Query q = new QueryParser(Version.LUCENE_36, CONTENT, analyzer).parse(query);
		IndexSearcher searcher = new IndexSearcher(idx, true);
		TopScoreDocCollector collector = TopScoreDocCollector.create(10000, true);
		searcher.search(q, collector);
		ScoreDoc[] hits = collector.topDocs().scoreDocs;
		double maxScore = 0;
		double minScore = Double.MAX_VALUE;
		long ini = System.currentTimeMillis();
		for (int i = 0; i < hits.length; i++) {
			int docID = hits[i].doc;
			Document d = searcher.doc(docID);
			if(hits[i].score>maxScore)
				maxScore=hits[i].score;
			if(hits[i].score<minScore)
				minScore=hits[i].score;
		}
		long fin = System.currentTimeMillis();
		searcher.close();
		System.out.println("-----------------------"+query+"-----------------------");
		System.out.println("Results: "+hits.length);
		System.out.println("Max: "+maxScore);
		System.out.println("Min: "+minScore);
		System.out.println("Time: "+(fin-ini));
		for (int i = 0; i < 10 && i<hits.length; i++) {
			System.out.println("\t"+hits[i].score);
		}
		System.out.println("---------------------------------------------------");
	}
	
	public static void main(String[] args) throws CorruptIndexException, LockObtainFailedException, IOException, ParseException {
		SearchEngine engine = SearchEngine.darInstancia();
		String[] queries = {
				"flat",
				"head",
				"bill",
				"green"
				};
		for (int i = 0; i < queries.length; i++) {
			String actual = queries[i];
			engine.search(actual);
		}
	}
}